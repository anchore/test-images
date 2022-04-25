# hadolint ignore=DL3006
# oraclelinux:7-slim
FROM oraclelinux@sha256:8e23381802e207aa9dee2e27ee85812f645735e2572482f52ab767de60b29126

WORKDIR /sandbox

COPY ./pom.xml pom.xml

ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.332.b09-1.el7_9.x86_64/jre

# hadolint ignore=DL3015,DL4006
RUN yum install wget-1.14-18.el7_6.1 -y && \
wget --quiet http://repos.fedorapeople.org/repos/dchen/apache-maven/epel-apache-maven.repo -O /etc/yum.repos.d/epel-apache-maven.repo && \
yum install ruby-2.0.0.648-39.el7_9 -y && \
yum install gcc-4.8.5-28.0.1.el7 python3-devel-3.6.8-18.0.5.el7 -y && \
yum install python3-3.6.8-18.0.5.el7 python3-pip-9.0.3-8.0.1.el7 -y && \
yum install apache-maven-3.5.2-1.el7 -y && \
yum install oracle-nodejs-release-el7-1.0-9.el7 -y && \
yum install nodejs-16.14.2-1.0.1.el7 -y && \
gem install ftpd -v 0.2.1 && \
npm install xmldom@0.4.0 && \
pip3 install --no-cache-dir aiohttp==3.7.3 && \
mvn clean install && mvn package && \
yum remove ruby gcc python3-devel python3-pip python3 java-11-openjdk maven nodejs wget oracle-nodejs-release-el7 -y && \
yum clean all && \
rm -rf /var/cache/yum && \
rm -rf /root/.m2
