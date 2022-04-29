FROM ubuntu@sha256:20858ebbc96215d6c3c574f781133ebffdc7c18d98af4f294cc4c04871a6fe61

WORKDIR /sandbox

RUN set -ex && \
    echo "deb http://old-releases.ubuntu.com/ubuntu/ wily main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu/ wily-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://old-releases.ubuntu.com/ubuntu/ wily-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    apt-get update -y && \
    apt-get install -y --no-install-recommends nginx-common=1.9.15-0ubuntu1 nginx-full=1.9.15-0ubuntu1 nginx=1.9.15-0ubuntu1 && \
    apt-get autoremove -y && \
    rm -rf /root/.m2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
