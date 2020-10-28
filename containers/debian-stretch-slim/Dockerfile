# hadolint ignore=DL3006
FROM debian:stretch-slim

ARG DEBIAN_FRONTEND=noninteractive

RUN set -ex && \
    apt-get update && \
    apt-get --assume-yes -q install --no-install-recommends cron-apt=0.10.0 && rm -rf /var/lib/apt/lists/*

