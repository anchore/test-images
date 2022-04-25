# amazonlinux:2.0.20210126.0
FROM amazonlinux@sha256:3c663506cf84b035d68c6450c48f76092821736d6b0615d8bd45f3caf525abe7

WORKDIR /sandbox

COPY ./pom.xml pom.xml

# hadolint ignore=DL3015,DL4006
RUN curl -fsSL https://rpm.nodesource.com/setup_12.x | bash - && \ 
yum install ruby-2.0.0.648 -y && \
yum install gcc-7.3.1-5.amzn2.0.2 python-3-devel-3.7.0-0.20.rc1.amzn2.0.2 -y && \
yum install python3-3.7.0-0.20.rc1.amzn2.0.2 python3-pip-20.2.2-1.amzn2.0.3 -y && \
yum install java-1.8.0-openjdk-1.8.0.222.b03-1.amzn2.0.1 maven-3.0.5-17.amzn2 -y && \
yum install nodejs-12.22.12-1nodesource -y && \
gem install ftpd -v 0.2.1 && \
npm install xmldom@0.4.0 && \
pip3 install --no-cache-dir aiohttp==3.7.3 && \
mvn clean install && mvn package && \
yum remove ruby gcc python3-devel python3-pip python3 java-1.8.0-openjdk maven nodejs -y && \
yum clean all && \
rm -rf /var/cache/yum && \
rm -rf /root/.m2
