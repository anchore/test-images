# syft and grype both used to get flagged with false positives on go-protobuf
FROM docker.io/anchore/grype:v0.46.0@sha256:6ccf6ac23f90fde7ea202ce2b18d6ad98d3e8992c73455841167afa27a71d93d as grype
FROM docker.io/anchore/syft:v0.53.4@sha256:37e85e8efdeaabb1b6f65c5bc175b664cb05d1aaddd0d922130b8e25d6e49726 as syft
# Include a much older version of syft with some legitimate vulns as well as fps
FROM docker.io/anchore/syft:v0.29.0@sha256:ad976e67541f2d5a50c9824377ea0d05e5f571e1ab6b313f2b2df37a60677043 as syft-v0.29.0

FROM scratch

COPY --from=grype /grype /usr/local/bin/grype
COPY --from=syft /syft /usr/local/bin/syft
COPY --from=syft-v0.29.0 /syft /usr/local/bin/syft-v0.29.0
