FROM registry.access.redhat.com/ubi8/ubi:8.6@sha256:8ce9caf9d86c83b47bda7c73a8fafb5fcf17f56ea13c050408cfb59aae28ae98

RUN yum update -y && \
    # install repositories for postgres & hivex packages \
    case $(uname -m) in \
      "x86_64") \
        yum install -y \
        http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/Packages/centos-stream-repos-8-2.el8.noarch.rpm \
        http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/Packages/centos-gpg-keys-8-2.el8.noarch.rpm \
        ;; \
      "aarch64") \
        yum install -y \
        http://mirror.centos.org/centos/8-stream/BaseOS/aarch64/os/Packages/centos-stream-repos-8-2.el8.noarch.rpm \
        http://mirror.centos.org/centos/8-stream/BaseOS/aarch64/os/Packages/centos-gpg-keys-8-2.el8.noarch.rpm \
        ;; \
    esac && \
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
