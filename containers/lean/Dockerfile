# hadolint ignore=DL3006
FROM alpine

# install ruby
RUN apk --no-cache add ruby=2.7.1-r3 ruby-dev=2.7.1-r3

# clear after install
RUN rm -rf /var/cache/apk/*

#install bundler
RUN gem install bundler:2.1.4

# create WORKDIR
ENV WORKDIR /srv/current
RUN mkdir $WORKDIR
WORKDIR $WORKDIR
