FROM alpine
RUN \
  # update packages
  apk update && apk upgrade && \

  # install ruby
  apk --no-cache add ruby ruby-dev && \

  # clear after install
  rm -rf /var/cache/apk/* \
  
  #install bundler
  gem install bundler


# use mounted volume for gems
ENV BUNDLE_PATH /bundle

# create WORKDIR
ENV WORKDIR /srv/current
RUN mkdir $WORKDIR
WORKDIR $WORKDIR