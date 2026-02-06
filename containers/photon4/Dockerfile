# Photon OS 4.0 test image
FROM photon:4.0
LABEL maintainer="Anchore Test"
# Update image and install some packages with known vulnerabilities for testing
# hadolint ignore=DL3041
RUN tdnf update -y && tdnf clean all
RUN tdnf install -y curl vim && tdnf clean all
