# hadolint ignore=DL3006
FROM alpine

RUN wget -nv https://repo1.maven.org/maven2/junit/junit/4.13.1/junit-4.13.1.jar && \
    wget -nv https://get.jenkins.io/plugins/TwilioNotifier/0.2.1/TwilioNotifier.hpi && \
    wget -nv https://updates.jenkins-ci.org/download/war/1.390/hudson.war && \
    wget -nv https://get.jenkins.io/plugins/nomad/0.7.4/nomad.hpi

COPY build/example-java-app-gradle-0.1.0.ear /
