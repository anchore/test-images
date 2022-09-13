FROM docker.io/library/ruby:3.0@sha256:5175a99b2d015ff9472b3bdcca5b3535da80fcaa3ecf5ed4558ed6c87f14d01d as ruby

WORKDIR /packages
COPY Gemfile Gemfile.lock /packages/

RUN bundle config set --local deployment 'true' && \
    bundle config set --local frozen 'true' && \
    bundle install

FROM scratch

COPY --from=ruby /packages/ /usr/local/packages/ruby/
