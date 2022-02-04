# hadolint ignore=DL3006
FROM registry.access.redhat.com/ubi8/ubi
LABEL maintainer="Anchore Test"
# Update image
# hadolint ignore=DL3033
RUN yum update --disableplugin=subscription-manager -y && rm -rf /var/cache/yum
RUN yum install --disableplugin=subscription-manager cronie openscap -y && yum clean all
