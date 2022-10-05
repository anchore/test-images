FROM quay.io/centos/centos:stream8@sha256:c9acf46f90fcb637eff59e269fbbebf5ec9e6b6215a07fbe2bbad7429aad6e7e

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
