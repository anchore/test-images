NAME := $(shell pwd | rev | cut -d '/' -f 1 | rev)
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
lint: ## TODO: with hadolint or similar
	$(call title,Building container image anchore/test_image:$(NAME))
	docker run --rm -i hadolint/hadolint < Dockerfile

.PHONY: build
build: ## build container with the current Dockerfile
	$(call title,Building container image anchore/test_image:$(NAME))
	docker build -t anchore/test_images:$(NAME) .

.PHONY: push
push: ## push built container to Docker Hub
	$(call title,Pushing container image to docker hub anchore/test_image:$(NAME))
	docker build -t anchore/test_images:$(NAME) .
	docker push anchore/test_images:$(NAME)

.PHONY: clean
clean: ## Remove images with the assigned tag for test_images
	$(call title,Removing image anchore/test_image:$(NAME))
	docker rmi anchore/test_images:$(NAME)
