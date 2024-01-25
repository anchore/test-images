FROM registry.access.redhat.com/ubi9/ubi-minimal:9.3-1475@sha256:a340f4b9fb261a75c84666a3dccb88e193a116da3cebabaf9bcdc33609b61172

RUN microdnf install -y nodejs-1:16.20.2-3.el9_2 && \
    microdnf clean all
