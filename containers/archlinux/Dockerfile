# Arch Linux test container with known vulnerable packages
# Uses the Arch Linux Archive to install specific older package versions

FROM docker.io/archlinux/archlinux@sha256:d6869c0af41f1bd0495a038fc4ada04c05ef9094bcf012db087f79a3b8f1b3c2

WORKDIR /sandbox

# Install packages with known vulnerabilities:
#
# From archive (2023-01-15) - fixed vulnerabilities for testing version comparison:
# - curl 7.87.0-3: CVE-2023-23914, CVE-2023-23915, CVE-2023-23916
# - vim 9.0.1178-1: CVE-2023-0433, CVE-2023-0288, CVE-2023-0054
# - openssl 3.0.7-4: CVE-2023-0286, CVE-2023-0215, CVE-2022-4450, CVE-2022-4304
# - sqlite 3.40.1-1: CVE-2022-46908
#
# From current repos - unfixed vulnerability for testing "no fix available":
# - pam: AVG-2901 / CVE-2025-6020 (arbitrary filesystem access, High severity, no fix)
#
# Python package for testing ownership-by-file-overlap deduplication:
# - python-urllib3 1.26.20 (from 2024-11-01 archive): CVE-2025-66471 (affects >=1.0,<2.6.0)
#   Syft detects both ALPM package AND embedded Python package,
#   enabling test of comprehensiveDistros deduplication (arch-cmm)
#
# hadolint ignore=SC2016
RUN echo 'Server=https://archive.archlinux.org/repos/2023/01/15/$repo/os/$arch' > /etc/pacman.d/mirrorlist && \
    sed -i 's/SigLevel.*/SigLevel = Never/' /etc/pacman.conf && \
    pacman -Syy --noconfirm && \
    pacman -S --noconfirm --needed \
      curl \
      vim \
      openssl \
      sqlite && \
    echo 'Server=https://geo.mirror.pkgbuild.com/$repo/os/$arch' > /etc/pacman.d/mirrorlist && \
    pacman -Syy --noconfirm && \
    pacman -S --noconfirm --needed pam && \
    echo 'Server=https://archive.archlinux.org/repos/2024/11/01/$repo/os/$arch' > /etc/pacman.d/mirrorlist && \
    pacman -Syy --noconfirm && \
    pacman -S --noconfirm --needed python-requests && \
    rm -rf /var/cache/pacman/pkg/*
