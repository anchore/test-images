FROM alpine@sha256:2bb501e6173d9d006e56de5bce2720eb06396803300fe1687b58a7ff32bf4c14

RUN set -ex && \
	echo 'http://dl-cdn.alpinelinux.org/alpine/v3.7/main' >> /etc/apk/repositories && \
	apk --no-cache add git=2.15.4-r0 && \
	rm -rf /var/cache/apk/* && \
    rm -rf /root/.m2