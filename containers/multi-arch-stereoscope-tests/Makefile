LAST_COMMIT := $(shell git rev-parse HEAD | cut -c 1-7)
NAME := $(shell pwd | rev | cut -d '/' -f 1 | rev)-$(LAST_COMMIT)
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

.PHONY: lint
lint:
	$(call title,Building container image anchore/test_image:$(NAME) variants)
	docker run --rm -i hadolint/hadolint hadolint --ignore DL3033 - < Dockerfile

.PHONY: build
build:
	$(call title,Building container image anchore/test_image:$(NAME) variants)
	docker build -t anchore/test-images:$(NAME)-amd64-only --build-arg ARCH=linux/amd64 .
	docker build -t anchore/test-images:$(NAME)-s390x-only --build-arg ARCH=linux/s390x .
	docker build -t anchore/test-images:$(NAME)-arm64-only --build-arg ARCH=linux/arm64 .

.PHONY: push
push: build ## push built container to Docker Hub
	$(call title,Pushing container image to docker hub anchore/test_image:$(NAME) variants)
	docker push anchore/test-images:$(NAME)-amd64-only
	docker push anchore/test-images:$(NAME)-s390x-only
	docker push anchore/test-images:$(NAME)-arm64-only
	docker manifest create \
	anchore/test-images\:$(NAME)-no-arm64 \
	--amend anchore/test-images\:$(NAME)-amd64-only \
	--amend anchore/test-images\:$(NAME)-s390x-only
	docker push anchore/test-images\:$(NAME)-no-arm64
	docker manifest create \
	anchore/test-images\:$(NAME)-no-amd64 \
	--amend anchore/test-images\:$(NAME)-s390x-only \
	--amend anchore/test-images\:$(NAME)-arm64-only
	docker push anchore/test-images\:$(NAME)-no-amd64

.PHONY: clean
clean: ## Remove images with the assigned tag for test_images
	$(call title,Removing image anchore/test_image:$(NAME) variants)
	docker rmi anchore/test-images:$(NAME)-amd64-only
	docker rmi anchore/test-images:$(NAME)-s390x-only
	docker rmi anchore/test-images:$(NAME)-arm64-only
