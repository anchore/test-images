# `sles-15.7-python-3.11.14`
A SLES 15.7 python base image with the SLES python 3.11.14 package and the following SLES python 3 RPM packages
- FROM registry.suse.com/bci/python:3.11.14
#FROM registry.suse.com/suse/sle15:15.6

RUN zypper --non-interactive install -y --no-recommends \
	python3-Werkzeug \
	python3-requests \
