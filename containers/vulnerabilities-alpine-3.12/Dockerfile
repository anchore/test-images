FROM alpine@sha256:c75ac27b49326926b803b9ed43bf088bc220d22556de1bc5f72d742c91398f69

RUN set -ex && \
	echo 'http://dl-cdn.alpinelinux.org/alpine/v3.11/main' >> /etc/apk/repositories && \
	echo 'http://dl-cdn.alpinelinux.org/alpine/v3.7/main' >> /etc/apk/repositories && \
	apk --no-cache add git=2.24.4-r0 && \
	apk --no-cache add jq=1.5-r5 && \
	rm -rf /var/cache/apk/* && \
    rm -rf /root/.m2