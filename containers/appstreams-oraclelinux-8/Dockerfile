FROM docker.io/library/oraclelinux:8.6@sha256:d3481ceaac964400f4d5006511d41d7772361570cb89b4f7e4ab759fa8902c73

RUN yum update -y && \
    yum module enable -y \
        postgresql:12 \
        ruby:2.5 \
        php:7.4 \
        nodejs:14 \
        nginx:1.16 \
        maven:3.5 \
        mariadb:10.3 && \
    yum install -y \
        postgresql \
        ruby \
        php \
        nodejs \
        nginx \
        maven \
        mariadb && \
    yum clean all
