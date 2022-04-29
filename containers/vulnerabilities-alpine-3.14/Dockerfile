FROM alpine@sha256:06b5d462c92fc39303e6363c65e074559f8d6b1363250027ed5053557e3398c5

RUN set -ex && \
	echo 'http://dl-cdn.alpinelinux.org/alpine/v3.11/main' >> /etc/apk/repositories && \
	apk --no-cache add vim=8.2.3437-r0 && \
	rm -rf /var/cache/apk/* && \
    rm -rf /root/.m2