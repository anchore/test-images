# hadolint ignore=DL3006
FROM ubuntu@sha256:10cbddb6cf8568f56584ccb6c866203e68ab8e621bb87038e254f6f27f955bbe

WORKDIR /sandbox

COPY ./pom.xml pom.xml

# hadolint ignore=DL3015
RUN apt-get update && \
    apt-get install -y ruby-full=1:2.7+1  && \
    apt-get install -y python3=3.8.2-0ubuntu2 && \
    apt-get -y install python3-pip=20.0.2-5ubuntu1.6   && \
    mkdir -p /usr/share/man/man1 && \
    export DEBIAN_FRONTEND=noninteractive && \
    export TZ=America/New_York && \
    apt-get install -y openjdk-11-jdk=11.0.11+9-0ubuntu2~20.04   && \
    apt-get install -y maven=3.6.3-1 && \
    apt-get install -y nodejs=10.19.0~dfsg-3ubuntu1  npm=6.14.4+ds-1ubuntu2 && \
    gem install figaro -v 1.2.0 && \
    npm install lodash@4.17.21 && \
    pip3 install --no-cache-dir numpy==1.21.2 && \
    mvn clean install && mvn package  && \
    apt-get remove -y ruby-full python3 python3-pip npm nodejs openjdk-11-jdk maven && \
    apt-get autoremove -y && \
    rm -rf /root/.m2 && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
