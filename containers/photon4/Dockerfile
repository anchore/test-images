# Photon OS 4.0 test image with pinned vulnerable packages
FROM photon:4.0
LABEL maintainer="Anchore Test"

# Install specific vulnerable versions for testing
# hadolint ignore=DL3041
RUN tdnf install -y \
    curl-8.12.0-1.ph4 \
    curl-libs-8.12.0-1.ph4 \
    expat-libs-2.7.1-1.ph4 \
    openssl-3.0.16-2.ph4 \
    && tdnf clean all
