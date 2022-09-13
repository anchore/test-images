FROM docker.io/library/python:3.9-slim@sha256:031f73dcb29e616220ea3acf6cce822226f17971647cd682909d7c6a87feffd2 as python

WORKDIR /packages
COPY requirements-lock.txt /packages

RUN pip install --no-cache-dir -r requirements-lock.txt -t . --disable-pip-version-check

FROM scratch

COPY --from=python /packages/ /usr/local/packages/python/
