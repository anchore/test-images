# hadolint ignore=DL3006
FROM centos:8

# Custom hints for packages
ADD anchore_hints.json /
# install Python3, and uses pip to install pytest
# finally it removes the cache - all in one go to prevent another layer which we don't need
RUN set -ex && \
    yum install -y cronie-1.5.2 && \
    yum clean all
