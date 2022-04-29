FROM alpine@sha256:bcae378eacedab83da66079d9366c8f5df542d7ed9ab23bf487e3e1a8481375d

RUN set -ex && \
	echo 'http://dl-cdn.alpinelinux.org/alpine/v3.10/main' >> /etc/apk/repositories && \
	apk --no-cache add curl=7.66.0-r4 && \
	rm -rf /var/cache/apk/* && \
    rm -rf /root/.m2