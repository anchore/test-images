# hadolint ignore=DL3006
FROM ubuntu@sha256:9d42d0e3e57bc067d10a75ee33bdd1a5298e95e5fc3c5d1fce98b455cb879249

# Install packages that have known false-positive needs-triage entries where
# ESM confirms not-affected. Used to validate ESM not-affected inference in the
# vunnel ubuntu provider quality gate.
#
# source package (binary installed)     delta  ESM reason
# x11vnc                                  5    not-affected
# nasm                                    5    not-affected / code not present
# fig2dev                                 3    code not present
# hadolint ignore=DL3008
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        x11vnc \
        nasm \
        fig2dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
