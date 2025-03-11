LAST_COMMIT := $(shell git rev-parse HEAD | cut -c 1-7)
NAME := $(shell pwd | rev | cut -d '/' -f 1 | rev)-$(LAST_COMMIT)
TEMPDIR = ./.tmp
IMAGEDIRS = $(shell ls -d containers/* | cut -d '/' -f 2)
BOLD := $(shell tput -T linux bold)
PURPLE := $(shell tput -T linux setaf 5)
GREEN := $(shell tput -T linux setaf 2)
CYAN := $(shell tput -T linux setaf 6)
RED := $(shell tput -T linux setaf 1)
RESET := $(shell tput -T linux sgr0)
TITLE := $(BOLD)$(PURPLE)
SUCCESS := $(BOLD)$(GREEN)

define title
    @printf '$(TITLE)$(1)$(RESET)\n'
endef


.PHONY: all
all: lint build
	@printf '$(SUCCESS)All checks pass!$(RESET)\n'

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(BOLD)$(CYAN)%-25s$(RESET)%s\n", $$1, $$2}'


.PHONY: lint
lint:
	$(call Skipping Lint for $(NAME))

.PHONY: build
build: ## build container with the current Dockerfile
# If a setup.sh is defined in the target's directory, then execute it. This is
# conditional because not all targets have a scripts/setup.sh
ifneq ("$(wildcard scripts/setup.sh)", "")
	./scripts/setup.sh
endif
	export DOCKER_CLI_EXPERIMENTAL=enabled; \
	docker manifest create \
	anchore/test_images:$(NAME)\
	--amend alpine@sha256:13fceee8faadd52b154af4b9af3f6740d45a431b10c4a20da6ca1178ec487151 \
	--amend alpine@sha256:afc845fd4ceb5a904087066567df0c2232929290e642c47c920227e65dc9937c

.PHONY: push
push: build ## push built container to Docker Hub
	$(call title,Pushing manifest list to docker hub anchore/test_image:$(NAME))
	export DOCKER_CLI_EXPERIMENTAL=enabled; \
	docker manifest push anchore/test_images:$(NAME)

.PHONY: clean
clean: ## Remove images with the assigned tag for test_images
	$(call title,Removing image anchore/test_image:$(NAME))
	export DOCKER_CLI_EXPERIMENTAL=enabled; \
	docker manifest rm anchore/test_images:$(NAME)
