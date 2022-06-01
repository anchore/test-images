FROM alpine@sha256:4edbd2beb5f78b1014028f4fbb99f3237d9561100b6881aabbf5acce2c4f9454

# For the E2E Test for Retrieved Files, nothing needs to be done, since alpine:latest comes baked with a /etc/passwd file
# and by helm chart default, the Anchore Analyzer will pull it out

# For the Content Search, we need to throw a file we know in the image
COPY ./anchore-e2e-content-search-test.txt /anchore-e2e-content-search-test.txt