# `archlinux`

An Arch Linux test image with packages from a point-in-time snapshot known to have vulnerabilities. Uses the Arch Linux Archive to install specific older versions.

## Archive Date

2023-01-15 - This snapshot contains packages with multiple known CVEs that were fixed in later releases.

## Installed Packages

### From Archive (2023-01-15) - Fixed Vulnerabilities
* curl 7.87.0-3 - CVE-2023-23914, CVE-2023-23915, CVE-2023-23916
* vim 9.0.1178-1 - CVE-2023-0433, CVE-2023-0288, CVE-2023-0054, CVE-2023-0049
* openssl 3.0.7-4 - CVE-2023-0286, CVE-2023-0215, CVE-2022-4450, CVE-2022-4304
* sqlite 3.40.1-1 - CVE-2022-46908

### From Current Repos - Unfixed Vulnerability
* pam (latest) - AVG-2901 / CVE-2025-6020 (High severity, no fix available)

## Purpose

Used to verify the Arch Linux provider correctly identifies vulnerabilities in scanned images against the archlinux:rolling namespace vulnerability database.
