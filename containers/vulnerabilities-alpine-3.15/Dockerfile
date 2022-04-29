FROM alpine@sha256:4edbd2beb5f78b1014028f4fbb99f3237d9561100b6881aabbf5acce2c4f9454

RUN set -ex && \
	echo 'http://dl-cdn.alpinelinux.org/alpine/v3.11/main' >> /etc/apk/repositories && \
	apk --no-cache add vim=8.2.3437-r0 && \
	rm -rf /var/cache/apk/* && \
    rm -rf /root/.m2