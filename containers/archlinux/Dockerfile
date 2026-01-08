# Arch Linux test image with vulnerable packages from archive snapshots.
# See README.md for package list.

FROM docker.io/archlinux/archlinux@sha256:d6869c0af41f1bd0495a038fc4ada04c05ef9094bcf012db087f79a3b8f1b3c2

WORKDIR /sandbox

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
