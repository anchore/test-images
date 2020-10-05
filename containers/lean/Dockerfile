FROM alpine

# update packages
RUN apk update && apk upgrade

# install ruby
RUN apk --no-cache add ruby ruby-dev

# clear after install
RUN rm -rf /var/cache/apk/*
  
#install bundler
RUN gem install bundler

# create WORKDIR
ENV WORKDIR /srv/current
RUN mkdir $WORKDIR
WORKDIR $WORKDIR