# test-images
This repository holds files like `Dockerfile` with some automation to build container images used for testing.


## Development

If you need to create a new container for testing, create a new directory with a Dockerfile and symlink the `ContainerMakefile` into it. So far, `make build` is the only command supported.
