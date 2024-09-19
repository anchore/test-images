# vex-oci-attach

This image is meant to capture both an image for analysis as well as VEX documents attached to the OCI registry.

The following references were used as a basis:

```
grype ubuntu:24.04@sha256:c279a739b31ead4ebc3e9ce04937eb8b612799b52c26133eb3b4a056d08c31a6 -o json | jq '.matches[] | [.vulnerability.id, .artifact.purl]'
```

```json
[
  "CVE-2016-2781",
  "pkg:deb/ubuntu/coreutils@9.4-3ubuntu6?arch=amd64&distro=ubuntu-24.04"
]
[
  "CVE-2022-3219",
  "pkg:deb/ubuntu/gpgv@2.4.4-2ubuntu17?arch=amd64&upstream=gnupg2&distro=ubuntu-24.04"
]
[
  "CVE-2016-20013",
  "pkg:deb/ubuntu/libc-bin@2.39-0ubuntu8.2?arch=amd64&upstream=glibc&distro=ubuntu-24.04"
]
[
  "CVE-2016-20013",
  "pkg:deb/ubuntu/libc6@2.39-0ubuntu8.2?arch=amd64&upstream=glibc&distro=ubuntu-24.04"
]
[
  "CVE-2024-2236",
  "pkg:deb/ubuntu/libgcrypt20@1.10.3-2build1?arch=amd64&distro=ubuntu-24.04"
]
[
  "CVE-2020-22916",
  "pkg:deb/ubuntu/liblzma5@5.6.1%2Breally5.4.5-1?arch=amd64&upstream=xz-utils&distro=ubuntu-24.04"
]
[
  "CVE-2024-4741",
  "pkg:deb/ubuntu/libssl3t64@3.0.13-0ubuntu3.1?arch=amd64&upstream=openssl&distro=ubuntu-24.04"
]
[
  "CVE-2024-4603",
  "pkg:deb/ubuntu/libssl3t64@3.0.13-0ubuntu3.1?arch=amd64&upstream=openssl&distro=ubuntu-24.04"
]
[
  "CVE-2024-2511",
  "pkg:deb/ubuntu/libssl3t64@3.0.13-0ubuntu3.1?arch=amd64&upstream=openssl&distro=ubuntu-24.04"
]
[
  "CVE-2023-7008",
  "pkg:deb/ubuntu/libsystemd0@255.4-1ubuntu8?arch=amd64&upstream=systemd&distro=ubuntu-24.04"
]
[
  "CVE-2023-7008",
  "pkg:deb/ubuntu/libudev1@255.4-1ubuntu8?arch=amd64&upstream=systemd&distro=ubuntu-24.04"
]
```

The attached vex document when applied properly should ignore the following matches:

- CVE-2016-2781:
  -  pkg:deb/ubuntu/coreutils@9.4-3ubuntu6?arch=amd64&distro=ubuntu-24.04

- CVE-2022-3219
  - pkg:deb/ubuntu/gpgv@2.4.4-2ubuntu17?arch=amd64&distro=ubuntu-24.04

- CVE-2016-20013
  - pkg:deb/ubuntu/libc-bin@2.39-0ubuntu8.2?arch=amd64&distro=ubuntu-24.04
  - pkg:deb/ubuntu/libc6@2.39-0ubuntu8.2?arch=amd64&distro=ubuntu-24.04

- CVE-2023-7008
  - pkg:deb/ubuntu/libsystemd0@255.4-1ubuntu8?arch=amd64&distro=ubuntu-24.04
  - pkg:deb/ubuntu/libudev1@255.4-1ubuntu8?arch=amd64&distro=ubuntu-24.04

The vex document (`vex.json`) itself has been attached to this OCI registry via the following command:

```bash
# in containers/vex-oci-attach
cosign attest --predicate ./vex.json --type openvex ghcr.io/anchore/test-images/vex-oci-attach@sha256:8b95adbdf01ad43043ea9b63d6ac56abbe0e81b67fe40a27c39b6b83488f70ce
```

The OCI image is hosted on [ghcr.io](https://github.com/anchore/test-images/pkgs/container/test-images%2Fvex-oci-attach) with the attachment (as of this writing) found at tag [sha256-8b95adbdf01ad43043ea9b63d6ac56abbe0e81b67fe40a27c39b6b83488f70ce.att](https://github.com/anchore/test-images/pkgs/container/test-images%2Fvex-oci-attach/228700186?tag=sha256-8b95adbdf01ad43043ea9b63d6ac56abbe0e81b67fe40a27c39b6b83488f70ce.att)


This can be used with `grype --vex-autodiscover`.
