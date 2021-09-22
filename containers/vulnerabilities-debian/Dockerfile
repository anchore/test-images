# hadolint ignore=DL3006
FROM debian@sha256:ca9003e9899b458d46b6ee6b040cf9e0d715acbc58e0615871f019c38ada8bc1

WORKDIR /sandbox

COPY ./pom.xml pom.xml

# hadolint ignore=DL3015
RUN apt-get update && \
    apt-get install -y ruby-full=1:2.5.1 && \
    apt-get install -y python3=3.7.3-1 && \
    apt-get -y install python3-pip=18.1-5  && \
    mkdir -p /usr/share/man/man1 && \
    apt-get install -y openjdk-11-jdk=11.0.12+7-2~deb10u1  && \
    apt-get install -y maven=3.6.0-1 && \
    apt-get install -y nodejs=10.24.0~dfsg-1~deb10u1 npm=5.8.0+ds6-4+deb10u2 && \
    gem install ftpd -v 0.2.1 && \
    npm install xmldom@0.4.0 && \
    pip3 install --no-cache-dir aiohttp==3.7.3 && \
    mvn clean install && mvn package  && \
    apt-get remove -y ruby-full python3 python3-pip npm nodejs openjdk-11-jdk maven && \
    apt-get autoremove -y && \
    rm -rf /root/.m2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
