FROM docker.io/library/maven:3.8.6-jdk-11-slim@sha256:2cb7c73ba2fd0f7ae64cfabd99180030ec85841a1197b4ae821d21836cb0aa3b as maven

WORKDIR /downloads

RUN curl -o chainsaw.zip "https://dlcdn.apache.org/logging/chainsaw/2.1.0/apache-chainsaw-2.1.0-bin.zip" 

WORKDIR /packages
COPY pom.xml /packages

RUN mvn clean install && mvn package

# hadolint ignore=DL3008
RUN apt-get update \
    && apt-get install unzip --no-install-recommends --assume-yes \
    && unzip /downloads/chainsaw.zip -d /packages

FROM scratch

COPY --from=maven /packages/ /usr/local/packages/maven/

