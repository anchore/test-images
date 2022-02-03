# hadolint ignore=DL3006
FROM registry.access.redhat.com/ubi8/ubi:8.1

# install Python3, and uses pip to install pytest
# finally it removes the cache - all in one go to prevent another layer which we don't need
RUN set -ex && \
    dnf install -y cronie && \
    dnf clean all
