# syft and grype both used to get flagged with false positives on go-protobuf
FROM docker.io/anchore/grype:v0.46.0 as grype
FROM docker.io/anchore/syft:v0.53.4 as syft
# Include a much older version of syft with some legitimate vulns as well as fps
FROM docker.io/anchore/syft:v0.29.0 as syft-v0.29.0
FROM docker.io/atlassian/jira-software:8.2.0 as jira-software

FROM docker.io/library/node:16.16.0-slim as nodejs

WORKDIR /packages/
COPY package-lock.json /packages/

RUN npm ci --ignore-scripts

FROM docker.io/library/ruby:3.0 as ruby

WORKDIR /packages
COPY Gemfile Gemfile.lock /packages/

RUN bundle config set --local deployment 'true' && \
    bundle config set --local frozen 'true' && \
    bundle install

FROM docker.io/library/python:3.9-slim as python

WORKDIR /packages
COPY requirements-lock.txt /packages

RUN pip install --no-cache-dir -r requirements-lock.txt -t . --disable-pip-version-check

FROM docker.io/library/maven:3.8.6-jdk-11-slim as maven

WORKDIR /packages
COPY pom.xml /packages

RUN mvn clean install && mvn package

FROM scratch

COPY --from=grype /grype /usr/local/bin/grype
COPY --from=syft /syft /usr/local/bin/syft
COPY --from=syft-v0.29.0 /syft /usr/local/bin/syft-v0.29.0
COPY --from=nodejs /packages/ /usr/local/packages/npm/
COPY --from=ruby /packages/ /usr/local/packages/ruby/
COPY --from=python /packages/ /usr/local/packages/python/
COPY --from=maven /packages/ /usr/local/packages/maven/
COPY --from=jira-software /opt/atlassian/jira/ /opt/atlassian/jira-software/
