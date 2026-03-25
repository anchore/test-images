FROM registry.suse.com/bci/python:3.11.14@sha256:ed5da42dbeb0885dfbd146e8042f2481911700b908082897cd6a53a512abdf11

# hadolint ignore=DL3059
RUN zypper --non-interactive install -y --no-recommends \
	python3-Werkzeug=1.0.1-150300.3.8.1 \
	python3-requests=2.25.1-150300.3.18.1 \
	&& zypper clean