# hadolint ignore=DL3006
FROM alpine

# install Python3, and uses pip to install pytest
# finally it removes the cache - all in one go to prevent another layer which we don't need
WORKDIR /app

RUN set -ex && \
# install nodejs to get npm, then install loadsh \
    apk add --no-cache nodejs=14.17.6-r0 npm=7.17.0-r0 && \
    npm install lodash@4.17.4 && \
    rm -rf /var/cache/apk/*
