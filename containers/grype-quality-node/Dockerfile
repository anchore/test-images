FROM docker.io/library/node:16.16.0-slim@sha256:34a3b4b7c2704ce52372c42b9b7945b41fe8eb98d74e8af472add0b599b6e1ff as nodejs

WORKDIR /packages/
COPY package-lock.json /packages/

RUN npm ci --ignore-scripts

FROM scratch
COPY --from=nodejs /packages/ /usr/local/packages/npm/
