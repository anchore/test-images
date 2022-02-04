FROM registry.access.redhat.com/ubi8/ubi
USER root
LABEL maintainer="Anchore Test"
# Update image
RUN yum update --disableplugin=subscription-manager -y && rm -rf /var/cache/yum
RUN yum install --disableplugin=subscription-manager cronie openscap -y && rm -rf /var/cache/yum

