# hadolint ignore=DL3006
FROM alpine

# install Python3, and uses pip to install pytest
# finally it removes the cache - all in one go to prevent another layer which we don't need
RUN set -ex && \
# install python, pip,  and pytest \
    apk add --no-cache python3=3.9.5-r1 && \
    python3 -m ensurepip && \
    pip3 install --no-cache-dir pytest==6.1.1 && \
    rm -rf /var/cache/apk/* && \
# remove dependencies \
    apk --no-cache del gmp ncurses-terminfo-base ncurses-libs readline yaml libgcc libstdc++ libgmpxx pkgconf gmp-dev && \
    apk --no-cache del python3 ca-certificates libbz2 expat libffi gdbm xz-libs sqlite-libs
