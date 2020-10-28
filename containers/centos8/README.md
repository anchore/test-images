# `centos8`
CentOS 8 base image with `nginx` installed.

## why?
Although the `centos:8` image would suffice, it is critical to be able to have a reproducible image that (potentially) does not change. There are
a few repercussions if the image gets modified for tests, like the image digest being altered.
