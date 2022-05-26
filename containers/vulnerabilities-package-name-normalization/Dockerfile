# hadolint ignore=DL3006
FROM python:3.8-slim as installer

WORKDIR /python/pip/

RUN pip install --no-deps --no-cache-dir --target .\
	PyYAML==5.1 \
	oslo.middleware==3.20.0 \
	Products.PluggableAuthService==2.5 \
	sopel-plugins.channelmgnt==1.0 \
	url_regex==1.0 \
	aiohttp-session==2.3.0

# Just copy over the installed language packages for the moment
FROM scratch

COPY --from=installer /python/pip /python/pip

