FROM registry.access.redhat.com/ubi9/ubi-minimal:9.2-717@sha256:35c99977ee5baa359bdc80f9ccc360644d2dbccb7462ca0fd97a23170a00cfd1

RUN microdnf module enable -y nodejs:18 && \
    microdnf install -y nodejs-1:18.18.2-2.module+el9.2.0.z+20408+7cb5fda5 && \
    microdnf clean all

