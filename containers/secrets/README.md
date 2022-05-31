# `secrets`
An Alpine base image with a bunch of fake secret files in the /home directory.
Used in analyzer tests.

## Usages
This image is used in E2E testing, if you make any modifications, make sure the tests/regression/api/default_deployment/images/artifacts/secrets/test_image_secret_search.py test is working still