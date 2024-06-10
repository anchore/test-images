FROM wordpress:cli-2.4-php8.0@sha256:2133caf65169d8b7c08d2f5d78fe914ab6b083c4be405534c00a961d5c3c741b

RUN wp core download && wp config --skip-check create --dbuser=user --dbname=name

# installing a plugin requires a DB connection, but we can cheat and just copy a snippet of the plugin
WORKDIR /
COPY wp-content wp-content

