FROM alpine@sha256:ccf92aa53bc6c3b25be2ad0cce80baec1778f007f7e076b0ffbd1b225d0b3a9b

RUN set -ex && \
	echo 'http://dl-cdn.alpinelinux.org/alpine/v3.7/main' >> /etc/apk/repositories && \
	apk --no-cache add zlib=1.2.11-r1 && \
	apk --no-cache add jq=1.5-r5 && \
	rm -rf /var/cache/apk/* && \
    rm -rf /root/.m2