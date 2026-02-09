# `photon4`
VMware Photon OS 4.0 base image with known vulnerable packages for testing.

## why?
This image is used to test Photon OS vulnerability scanning support in grype.
Photon OS uses tdnf (Tiny DNF) as its package manager and RPM packages.

## image pinning
The base image is pinned by digest rather than installing specific package versions
with tdnf. Photon OS repos only keep the latest version of each package, so pinning
RPM versions in `tdnf install` breaks as soon as a newer version supersedes them.
Pinning the base image digest locks all package versions reliably.
