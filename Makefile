SHELL := /usr/bin/env bash
CHANGEDCONTAINERDIRS := $(shell git diff HEAD~1 --name-only containers/ | cut -d '/' -f1,2 | uniq)
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
all: build
	@printf '$(SUCCESS)All checks pass!$(RESET)\n'

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(BOLD)$(CYAN)%-25s$(RESET)%s\n", $$1, $$2}'
	@for dir in $(shell ls containers); do \
		printf "$(BOLD)$(CYAN)%-25s$(RESET)Create the local %s container\n" $$dir $$dir; \
	done


.PHONY: lint
lint: ## Uses hadolint container to ensure Dockerfiles are clean
	@for dir in $(CHANGEDCONTAINERDIRS); do \
		echo "Linting container: $${dir}"; \
		pushd $${dir} || exit 1; \
		make lint || exit 1; \
		popd > /dev/null; \
	done

.PHONY: new-image
new-image: ## Stubs out a directory for a new container image to be added
	mkdir -p containers/$(name)
	pushd containers/$(name) && ln -s ../../ContainerMakefile Makefile && popd
	touch containers/$(name)/Dockerfile
	touch containers/$(name)/README.md


.PHONY: test
test: build link_check ## Lint first, and then build all containers


.PHONY: build
build: ## Create all containers in the containers sub directory
	@for dir in $(CHANGEDCONTAINERDIRS); do \
		echo "Building container: $${dir}"; \
		pushd $${dir} || exit 1; \
		make build || exit 1; \
		popd > /dev/null; \
	done

.PHONY: push
push: ## Create all containers and push them to docker hub
	@for dir in $(CHANGEDCONTAINERDIRS); do \
		echo "Pushing container: $${dir}"; \
		pushd $${dir} || exit 1; \
		make push || exit 1; \
		popd > /dev/null; \
	done


link_check: ## Make sure that all symlinks are correct
	@for makefile in $(shell find containers -name Makefile); do \
		echo -n "Verifying Makefile link: $${makefile}"; \
		if [[ $$(readlink $${makefile}) != "../../ContainerMakefile" ]]; then echo "Path is not linked to ../../ContainerMakefile -> $${makefile}" && exit 1; fi; \
		echo "	[OK]"; \
	done

%: ## do a local build
	scripts/local.sh "$*"
