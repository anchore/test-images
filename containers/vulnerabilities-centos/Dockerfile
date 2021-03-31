# hadolint ignore=DL3006
FROM centos@sha256:e4ca2ed0202e76be184e75fb26d14bf974193579039d5573fb2348664deef76e

WORKDIR /sandbox

COPY ./pom.xml pom.xml

# hadolint ignore=DL3015
RUN yum install ruby-2.0.0.648 -y && \
yum install gcc-4.8.5 python3-devel-3.6.8 -y && \
yum install python3-3.6.8 python3-pip-9.0.3 -y && \
yum install java-11-openjdk-11.0.10.0.9 maven-3.0.5 -y && \
yum install epel-release-7 -y && \
yum install nodejs-6.17.1 -y && \
gem install ftpd -v 0.2.1 && \
npm install xmldom@0.4.0 && \
pip3 install --no-cache-dir aiohttp==3.7.3 && \
mvn clean install && mvn package && \
yum remove ruby gcc python3-devel python3-pip python3 java-11-openjdk maven nodejs epel-release -y && \
yum autoremove -y && \
yum clean all && \
rm -rf /var/cache/yum && \
rm -rf /root/.m2