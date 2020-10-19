# test-images
This repository holds files like `Dockerfile` with some automation to build container images used for testing.


## Development

If you need to create a new container for testing, create a new directory with a Dockerfile and symlink the `ContainerMakefile` into it. In this example
we create a `new` directory which will hold the contents for a new container image:

```text
$ mkdir containers/new
$ cd containers/new
$ ln -s ../../ContainerMakefile Makefile
```

After creating the new directory and symlinking the `ContainerMakefile` the automation will be able to make it part of its workflow to make it available on `anchore/test_images`.

Next, add a `Dockerfile` and make sure it passes the `build` and `lint` targets:

```
$ make lint
Linting container image anchore/test_image:new
docker run --rm -i hadolint/hadolint < Dockerfile
/dev/stdin:1 DL3006 Always tag the version of an image explicitly
make: *** [lint] Error 1
```

Since the tagging is done by the automation, add the following line at the top of the container:

```
# hadolint ignore=DL3006
```

That should allow the linting to pass. Create a pull request, which will also build and lint the container as part of the verification process.

After your container merges to the `main` branch, it will be pushed to `anchore/test_images`. Following the example in this section, it will tag it with the name
of the directory, which in this case is `new`. The end result will create the following container: `anchore/test_images:new`.


## make targets
A couple of other `make` commands are available for the symlinked `Makefile`, they are documented as part of the `make help` output.

* `make build`: builds the current container locally, tags it with the current directory name
* `make clean`: Removes the container image associated with the directory. If the directory name is `new`, then it will try to remove `anchore/test_images:new`
* `make lint`: Runs the `hadolint/hadolint` container passing the contents of the `Dockerfile` to stdin, this step is run as a verification when a PR is opened

In addition to defined targets, the `Makefile` supports dynamic targets by looking into the `containers/` directory. Every sub-directory in that path becomes an available target to build it locally. For example, `containers/py38` is exposed and available with the following command:

```
$ make py38
```
