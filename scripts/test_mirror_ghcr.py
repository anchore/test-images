import argparse
import os
import unittest
from subprocess import CompletedProcess
from unittest import mock

import mirror_ghcr as m

# real tags from `crane ls docker.io/anchore/test_images`
TAGS = [
    "alpine-multiarch-amd64-windows-linux-ba611b4",
    "alpine-multiarch-no-amd64-737dd8f",
    "centos8",
    "centos8-1c5465c",
    "centos8-56d52bc",
    "centos8-5f5b386",
    "centos8-7872316",
    "centos8-fa4a0d1",
    "distro_removed-5210dd6",
    "java",
    "java-56d52bc",
    "java_manifest_crash",
    "keycloak-2.4.0.Final",
    "neo4j-4.2.7-community",
    "sles-15.7-python-3.11.14-ac5a395",
    "sonarqube-6.5-alpine",
    "syft_bin-cf22714",
    "syft_bin-fb727c1",
    "tomcat-10.0.0-M8-jdk8",
    "ubi8-6bde59e",
    "vulnerabilities-alpine",
    "vulnerabilities-alpine-3.11-d5be50d",
    "vulnerabilities-alpine-56d52bc",
    "vulnerabilities-centos",
    "vulnerabilities-centos-56d52bc",
    "vulnerabilities-centos-5f5b386",
    "vulnerabilities-centos-7872316",
    "vulnerabilities-centos-f5e8952",
    "vulnerabilities-centos-stream9-ebc653b",
    "vulnerabilities-ubuntu-16.04-d5be50d",
]

# directories under containers/ at the time the tags above were captured; ubi8 was deleted
IMAGES = {
    "alpine-multiarch-amd64-windows-linux",
    "alpine-multiarch-no-amd64",
    "centos8",
    "distro_removed",
    "java",
    "sles-15.7-python-3.11.14",
    "syft_bin",
    "vulnerabilities-alpine",
    "vulnerabilities-alpine-3.11",
    "vulnerabilities-centos",
    "vulnerabilities-centos-stream9",
    "vulnerabilities-ubuntu-16.04",
}


def dest(**kw):
    return {i: kw.get(i) for i in IMAGES}


class ParseTag(unittest.TestCase):
    def test_repo_built(self):
        cases = {
            "java-56d52bc": ("java", "56d52bc"),
            "syft_bin-cf22714": ("syft_bin", "cf22714"),
            "sles-15.7-python-3.11.14-ac5a395": ("sles-15.7-python-3.11.14", "ac5a395"),
            "vulnerabilities-alpine-3.11-d5be50d": ("vulnerabilities-alpine-3.11", "d5be50d"),
            "vulnerabilities-alpine-56d52bc": ("vulnerabilities-alpine", "56d52bc"),
        }
        for tag, want in cases.items():
            self.assertEqual(m.parse_tag(tag), want, tag)

    def test_not_repo_built(self):
        for tag in ["java", "centos8", "java_manifest_crash", "tomcat-10.0.0-M8-jdk8", "sonarqube-6.5-alpine",
                    "neo4j-4.2.7-community", "keycloak-2.4.0.Final", "-56d52bc", "java-56D52BC", "java-56d52bcd"]:
            self.assertIsNone(m.parse_tag(tag), tag)


class Plan(unittest.TestCase):
    def rows(self, state):
        return m.plan(TAGS, IMAGES, state)

    def test_scope(self):
        got = {r[1] for r in self.rows(dest())}
        self.assertIn("ghcr.io/anchore/test-images/vulnerabilities-alpine-3.11:d5be50d", got)
        self.assertIn("ghcr.io/anchore/test-images/vulnerabilities-alpine:56d52bc", got)
        self.assertIn("ghcr.io/anchore/test-images/syft_bin:cf22714", got)
        self.assertIn("ghcr.io/anchore/test-images/sles-15.7-python-3.11.14:ac5a395", got)
        self.assertNotIn("ghcr.io/anchore/test-images/vulnerabilities-alpine:d5be50d", got)
        # deleted image, pre-sha tags and vendor tags
        self.assertFalse([g for g in got if "/ubi8:" in g or "/tomcat" in g or "/keycloak" in g])
        self.assertEqual(len(got), 20)

    def test_new_package_flag(self):
        self.assertTrue(all(new for _, _, new in self.rows(dest())))
        rows = self.rows(dest(centos8=set()))
        self.assertEqual({new for _, d, new in rows if "/centos8:" in d}, {False})
        self.assertTrue(all(new for _, d, new in rows if "/syft_bin:" in d))

    def test_existing_destination_tag_is_never_planned(self):
        rows = self.rows(dest(syft_bin={"cf22714", "fb727c1"}))
        self.assertFalse([d for _, d, _ in rows if "/syft_bin:" in d])
        got = {d for _, d, _ in self.rows(dest(syft_bin={"cf22714"}))}
        self.assertNotIn("ghcr.io/anchore/test-images/syft_bin:cf22714", got)
        self.assertIn("ghcr.io/anchore/test-images/syft_bin:fb727c1", got)

    def test_nothing_missing(self):
        full = {i: {p[1] for t in TAGS if (p := m.parse_tag(t)) and p[0] == i} for i in IMAGES}
        self.assertEqual(self.rows(full), [])


class Mirrored(unittest.TestCase):
    def test_pairs_are_tags_present_at_both_addresses(self):
        got = m.mirrored(TAGS, IMAGES, dest(syft_bin={"cf22714", "0000000"}, centos8=set()))
        self.assertEqual(got, [("docker.io/anchore/test_images:syft_bin-cf22714", "ghcr.io/anchore/test-images/syft_bin:cf22714")])


def done(rc=0, out="", err=""):
    return CompletedProcess([], rc, out, err)


def argvs(run):
    return [c.args[0] for c in run.call_args_list]


class CraneArgs(unittest.TestCase):
    def test_list_source(self):
        with mock.patch("mirror_ghcr.subprocess.run", return_value=done(out="a-1234567\n" * 800)) as run:
            m.list_source()
        self.assertEqual(argvs(run), [["crane", "ls", "docker.io/anchore/test_images"]])

    def test_list_dest(self):
        with mock.patch("mirror_ghcr.subprocess.run", return_value=done(out="abc1234\n")) as run:
            self.assertEqual(m.list_dest("java"), {"abc1234"})
        self.assertEqual(argvs(run), [["crane", "ls", "ghcr.io/anchore/test-images/java"]])

    def test_list_dest_name_unknown_is_missing_package(self):
        with mock.patch("mirror_ghcr.subprocess.run", return_value=done(1, err="NAME_UNKNOWN: repository name not known")):
            self.assertIsNone(m.list_dest("java"))

    def test_list_dest_other_error_aborts(self):
        with mock.patch("mirror_ghcr.subprocess.run", return_value=done(1, err="DENIED: requested access to the resource is denied")):
            with self.assertRaises(m.Abort):
                m.list_dest("java")

    def test_copy(self):
        rows = [("docker.io/anchore/test_images:java-56d52bc", "ghcr.io/anchore/test-images/java:56d52bc", True)]
        with mock.patch("mirror_ghcr.build_plan", return_value=([], {}, rows)), \
                mock.patch.dict(os.environ, {"GITHUB_ACTIONS": "true"}), \
                mock.patch("mirror_ghcr.subprocess.run", return_value=done()) as run:
            self.assertEqual(m.cmd_mirror(argparse.Namespace(yes=True)), 0)
        self.assertEqual(argvs(run), [["crane", "copy", rows[0][0], rows[0][1]]])

    def test_verify(self):
        src, dst = "docker.io/anchore/test_images:java-56d52bc", "ghcr.io/anchore/test-images/java:56d52bc"
        with mock.patch("mirror_ghcr.subprocess.run", return_value=done(out="sha256:aa\n")) as run:
            self.assertEqual(m.verify([(src, dst)]), 0)
        self.assertEqual(argvs(run), [["crane", "digest", src], ["crane", "digest", dst]])


if __name__ == "__main__":
    unittest.main()
