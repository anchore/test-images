FROM docker.io/almalinux:9.4@sha256:1c718a4cd7bab3bdb069ddbbd1eb593a390e6932d51d0048a2f6556303bafba7

RUN dnf install dnf-plugins-core -y && \
	dnf config-manager --set-enabled rt -y && \
	dnf install kernel-rt -y && \
    dnf clean all