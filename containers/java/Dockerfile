FROM anchore/test_images:grype-quality-java-d89207b@sha256:b3534fc2e37943136d5b54e3a58b55d4ccd4363d926cf7aa5bf55a524cf8275b as grype-quality-gate

# hadolint ignore=DL3006
FROM alpine

WORKDIR /packages

COPY --from=grype-quality-gate /usr/local/packages/maven/* /packages/
COPY build/example-java-app-gradle-0.1.0.ear /packages
COPY java_artifact_urls.txt /

RUN xargs -a /java_artifact_urls.txt wget -nv && \
    unzip ./gradle-7.1.1-bin.zip
