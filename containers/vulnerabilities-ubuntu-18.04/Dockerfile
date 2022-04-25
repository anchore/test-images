FROM ubuntu@sha256:86361bc18dd2964b8dc5971c82bf6c75b8515eb2dbfe879b76c5b149e8ca158a

WORKDIR /sandbox

COPY ./pom.xml pom.xml

RUN apt-get update && \
    apt-get install -y ruby-full=1:2.5.1 --no-install-recommends && \
    apt-get install -y python3.7=3.7.5-2ubuntu1~18.04.2 --no-install-recommends && \
    apt-get -y install python3-pip=9.0.1-2.3~ubuntu1.18.04.5 python3-setuptools=39.0.1-2 python3-wheel=0.30.0-0.2 --no-install-recommends  && \
    mkdir -p /usr/share/man/man1 && \
    apt-get install -y openjdk-11-jdk=11.0.15+10-0ubuntu0.18.04.1 --no-install-recommends  && \
    apt-get install -y maven=3.6.0-1~18.04.1 --no-install-recommends && \
    apt-get install -y nodejs=8.10.0~dfsg-2ubuntu0.4 npm=3.5.2-0ubuntu4 --no-install-recommends && \
    gem install ftpd -v 0.2.1 && \
    npm install xmldom@0.4.0 && \
    pip3 install --no-cache-dir aiohttp==3.7.3 && \
    mvn clean install && mvn package  && \
    apt-get remove -y ruby-full python3.7 python3-pip npm nodejs openjdk-11-jdk maven && \
    apt-get autoremove -y && \
    rm -rf /root/.m2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
