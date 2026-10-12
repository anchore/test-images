#!/usr/bin/env python3
"""Mirror repo-built tags from docker.io/anchore/test_images to ghcr.io/anchore/test-images.

A Docker Hub tag <dir>-<sha> becomes ghcr.io/anchore/test-images/<dir>:<sha>. Copies are
done with `crane copy`, which keeps manifest bytes (and so digests) identical.

  mirror_ghcr.py status         read-only summary of mirror progress
  mirror_ghcr.py mirror [--yes] print the plan, confirm, then copy
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

SOURCE = "docker.io/anchore/test_images"
DEST = "ghcr.io/anchore/test-images"

# a rate-limited or truncated listing must not read as "nothing to mirror". The registry
# held 878 tags when this was written and only grows.
MIN_SOURCE_TAGS = 800

CONTAINERS_DIR = Path(__file__).resolve().parent.parent / "containers"

SHA_RE = re.compile(r"[0-9a-f]{7}")
NOT_FOUND_RE = re.compile(r"NAME_UNKNOWN|name unknown|not found|404", re.IGNORECASE)


class Abort(Exception):
    pass


def parse_tag(tag):
    """Return (image, sha) for a repo-built tag, else None.

    Splits on the last '-' so that 'vulnerabilities-alpine-3.11-d5be50d' belongs to
    'vulnerabilities-alpine-3.11' and not to 'vulnerabilities-alpine'.
    """
    image, _, sha = tag.rpartition("-")
    if not image or not SHA_RE.fullmatch(sha):
        return None
    return image, sha


def plan(source_tags, images, dest_state):
    """Return sorted (source ref, destination ref, creates package) rows still missing.

    images is the set of directory names under containers/. dest_state maps an image to
    the set of tags already at the destination, or None when the package does not exist.
    An existing destination tag is never planned.
    """
    rows = []
    for tag in source_tags:
        parsed = parse_tag(tag)
        if parsed is None or parsed[0] not in images:
            continue
        image, sha = parsed
        have = dest_state[image]
        if have is not None and sha in have:
            continue
        rows.append((f"{SOURCE}:{tag}", f"{DEST}/{image}:{sha}", have is None))
    return sorted(rows)


def crane(*args, env=None):
    try:
        return subprocess.run(["crane", *args], capture_output=True, text=True, env=env)
    except FileNotFoundError:
        raise Abort("crane is not on PATH")


def list_source():
    res = crane("ls", SOURCE)
    if res.returncode != 0:
        raise Abort(f"listing {SOURCE} failed:\n{res.stderr.strip()}")
    tags = res.stdout.split()
    if len(tags) < MIN_SOURCE_TAGS:
        raise Abort(f"{SOURCE} returned {len(tags)} tags, expected at least {MIN_SOURCE_TAGS}; refusing to plan from a truncated listing")
    return tags


def list_dest(image):
    """Return the tags of a destination package, or None when the package does not exist."""
    res = crane("ls", f"{DEST}/{image}")
    if res.returncode == 0:
        return set(res.stdout.split())
    if NOT_FOUND_RE.search(res.stderr):
        return None
    # anything else (auth, rate limit, network) must not read as "package missing"
    raise Abort(f"listing {DEST}/{image} failed:\n{res.stderr.strip()}")


def build_plan():
    source_tags = list_source()
    images = {p.name for p in CONTAINERS_DIR.iterdir() if p.is_dir()}
    wanted = {p[0] for p in map(parse_tag, source_tags) if p and p[0] in images}
    dest_state = {image: list_dest(image) for image in sorted(wanted)}
    return source_tags, dest_state, plan(source_tags, images, dest_state)


def group_by_image(rows):
    groups = {}
    for src, dst, new in rows:
        groups.setdefault(dst.rsplit(":", 1)[0], []).append((src, dst, new))
    return groups


def print_plan(rows):
    for repo, group in group_by_image(rows).items():
        print(f"{repo}" + ("  (new package)" if group[0][2] else ""))
        for src, dst, _ in group:
            print(f"  {src} -> {dst}")
    new_pkgs = sum(1 for g in group_by_image(rows).values() if g[0][2])
    print(f"\n{len(rows)} tags to copy, {new_pkgs} new packages")


def cmd_mirror(args):
    _, _, rows = build_plan()
    if not rows:
        print("nothing to do")
        return 0
    print_plan(rows)

    if any(new for _, _, new in rows) and os.environ.get("GITHUB_ACTIONS") != "true":
        print(
            "\nrefusing to create packages outside GitHub Actions: a package created here is not "
            "linked to the repository and GITHUB_TOKEN could not push to it afterward.\n"
            "run `gh workflow run mirror-ghcr.yaml` instead.",
            file=sys.stderr,
        )
        return 1

    if not args.yes:
        if not sys.stdin.isatty():
            print("\nrefusing to apply without --yes", file=sys.stderr)
            return 1
        if input("\nApply? [y/N] ").strip().lower() not in ("y", "yes"):
            return 0

    for src, dst, _ in rows:
        print(f"copying {src} -> {dst}", flush=True)
        if subprocess.run(["crane", "copy", src, dst]).returncode != 0:
            print(f"copy failed: {src}", file=sys.stderr)
            return 1
    return 0


def cmd_status(_args):
    source_tags, dest_state, rows = build_plan()
    images = {p.name for p in CONTAINERS_DIR.iterdir() if p.is_dir()}
    built = sum(1 for t in source_tags if (p := parse_tag(t)) and p[0] in images)
    missing = len(rows)
    print(f"repo-built tags on Docker Hub: {built}")
    print(f"mirrored: {built - missing}")
    print(f"missing: {missing} ({100 * missing / built:.0f}%)" if built else "missing: 0")

    counts = {}
    for _, dst, _ in rows:
        repo = dst.rsplit(":", 1)[0]
        counts[repo] = counts.get(repo, 0) + 1
    if counts:
        print("\nimages with missing tags:")
        for repo, n in sorted(counts.items()):
            print(f"  {repo}: {n}")

    # probe with an empty docker config so no credential makes a private package look public
    private = []
    with tempfile.TemporaryDirectory() as empty:
        env = {**os.environ, "DOCKER_CONFIG": empty}
        for image, tags in sorted(dest_state.items()):
            if not tags:
                continue
            ref = f"{DEST}/{image}:{sorted(tags)[0]}"
            if crane("digest", ref, env=env).returncode != 0:
                private.append(f"{DEST}/{image}")
    if private:
        print("\npackages not readable anonymously:")
        for repo in private:
            print(f"  {repo}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="read-only summary of mirror progress").set_defaults(fn=cmd_status)
    mirror = sub.add_parser("mirror", help="print the plan, confirm, then copy")
    mirror.add_argument("--yes", action="store_true", help="apply without prompting")
    mirror.set_defaults(fn=cmd_mirror)
    args = parser.parse_args(argv)
    try:
        return args.fn(args)
    except Abort as e:
        print(f"error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
