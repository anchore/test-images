FROM alpine@sha256:66790a2b79e1ea3e1dabac43990c54aca5d1ddf268d9a5a0285e4167c8b24475

RUN set -ex && \
	echo 'http://dl-cdn.alpinelinux.org/alpine/v3.5/main' >> /etc/apk/repositories && \
	apk --no-cache add tiff=4.0.9-r6 && \
	rm -rf /var/cache/apk/* && \
    rm -rf /root/.m2