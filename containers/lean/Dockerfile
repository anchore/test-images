FROM alpine
RUN \
  # update packages
  apk update && apk upgrade && \

  # install ruby
  apk --no-cache add ruby ruby-dev ruby-bundler ruby-json ruby-irb ruby-rake ruby-bigdecimal && \

  # clear after install
  rm -rf /var/cache/apk/*

# to avoid installing documentation for gems
COPY gemrc $HOME/.gemrc

# use mounted volume for gems
ENV BUNDLE_PATH /bundle

# create WORKDIR
ENV WORKDIR /srv/current
RUN mkdir $WORKDIR
WORKDIR $WORKDIR