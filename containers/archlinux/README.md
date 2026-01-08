# `archlinux`

Arch Linux test image with packages from archive snapshots (2023-01-15, 2024-11-01).
Includes packages with known vulnerabilities:

* curl 7.87.0-3 - CVE-2023-23914, CVE-2023-23915
* vim 9.0.1178-1 - CVE-2023-0433, CVE-2023-0288
* openssl 3.0.7-4 - CVE-2023-0286, CVE-2022-4450
* sqlite 3.40.1-1 - CVE-2022-46908
* pam (current) - AVG-2901 (unfixed)
* python-requests 2.28.1-4 - includes python-urllib3 for deduplication testing

Used in arch provider quality gate tests.
