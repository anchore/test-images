# `vulnerabilities-ubuntu-20.04`

An Ubuntu 20.04 (focal) image with packages that have known false-positive vulnerability entries.

These packages have `needs-triage` status in the Ubuntu CVE tracker for focal, but the corresponding
ESM entries confirm `not-affected`. This image validates that the vunnel ubuntu provider's ESM
not-affected inference correctly suppresses these false positives.

## Installed packages and expected FP suppression

| Source package   | Binary installed           | Delta | ESM reason                                    |
|------------------|----------------------------|-------|-----------------------------------------------|
| x11vnc           | x11vnc                     | 5     | not-affected                                  |
| nasm             | nasm                       | 5     | not-affected / code not present               |
| fig2dev          | fig2dev                    | 3     | code not present                              |

"Delta" is the number of CVEs present in the reference grype DB but removed from the custom DB by the ESM inference change.
