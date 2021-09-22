FROM alpine@sha256:d1eaae2a6814b4b10a722fa75e8a6b53db42d1bf531395a107fea0458bfbf1d8

WORKDIR /sandbox

COPY ./pom.xml pom.xml

# install ruby, python, java, and nodejs 
# now install packages using GEM, NPM, PIP, and Java

RUN set -ex && \
    apk --no-cache add ruby=2.7.4-r0 && \
    apk --no-cache add gcc=9.3.0-r2 musl-dev=1.1.24-r10 && \
    apk --no-cache add python3=3.8.10-r0 python3-dev=3.8.10-r0 && \
    python3 -m ensurepip && \
    apk --no-cache add openjdk11=11.0.9_p11-r0  maven=3.6.3-r0 && \
    apk --no-cache add nodejs=12.22.6-r0 npm=12.22.6-r0 && \
    gem install ftpd -v 0.2.1 && \
    npm install xmldom@0.4.0 && \
    pip3 install --no-cache-dir aiohttp==3.7.3 && \
    mvn clean install && mvn package && \
    apk --no-cache del ruby gcc musl-dev python3 python3-dev openjdk11 maven nodejs npm && \
    rm -rf /var/cache/apk/* && \
    rm -rf /root/.m2