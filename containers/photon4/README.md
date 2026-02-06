# `photon4`
VMware Photon OS 4.0 base image with pinned vulnerable packages for testing.

## why?
This image is used to test Photon OS vulnerability scanning support in grype.
Photon OS uses tdnf (Tiny DNF) as its package manager and RPM packages.

## Pinned vulnerable packages
| Package     | Version      | CVEs                                              |
|-------------|--------------|---------------------------------------------------|
| curl        | 8.12.0-1.ph4 | CVE-2025-9086, CVE-2025-10148, CVE-2025-4947, CVE-2025-5025 |
| curl-libs   | 8.12.0-1.ph4 | CVE-2025-9086, CVE-2025-10148, CVE-2025-4947, CVE-2025-5025 |
| expat-libs  | 2.7.1-1.ph4  | CVE-2025-59375                                    |
| openssl     | 3.0.16-2.ph4 | CVE-2025-9230                                     |
