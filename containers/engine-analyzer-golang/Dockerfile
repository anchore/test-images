# hadolint ignore=DL3006
FROM docker.io/alpine:3.15.0 as go-src

WORKDIR /go/src

RUN apk add --no-cache git="2.34.1-r0" && \
    git clone --depth 1 --branch "v0.32.0" https://github.com/anchore/grype && \
    git clone --depth 1 --branch "v0.36.0" https://github.com/anchore/syft

FROM docker.io/anchore/grype:v0.32.0 as grype-binary
FROM docker.io/anchore/syft:v0.36.0 as syft-binary
FROM scratch

COPY --from=go-src /go/src/grype/go.mod /go/src/grype/
COPY --from=go-src /go/src/syft/go.mod /go/src/syft/

COPY --from=grype-binary /grype /usr/local/bin/
COPY --from=syft-binary /syft /usr/local/bin/
