SHELL := /bin/bash
GIT_SHA = $(shell git describe --tags --always)
GIT_BRANCH = $(shell git symbolic-ref --short -q HEAD)
BRANCH_VALID := $(shell [[ $(shell git symbolic-ref --short -q HEAD) =~ ^((release|feature|support|hotfix|bugfix)\/([a-zA-Z0-9][ A-Za-z0-9_.-]*)|(develop|staging|master))$$ ]] && echo matched)

all: image

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

image:         ## Build the docker image
	docker build --no-cache -t current -t morni .

dev-run:       ## Run app locally
	docker-compose up --force-recreate

dev-restart:       ## Run app locally
	docker-compose restart

celery-restart:       ## Run app locally
	docker-compose restart celery

dev-compose-state:       ## Listing app containers
	docker-compose ps

dev-logs:       ## Run app locally
	docker-compose logs -f --tail=100 app

dev-ssh:       ## SSH to the container
	docker-compose exec app bash

dev-down:      ## Tear down app
	docker-compose down

migrate:   ## Apply migrations
	docker-compose run app python manage.py migrate

shell:   ## Access the python shell
	docker-compose run app python manage.py shell

statics:   ## collect statics
	docker-compose run app python manage.py collectstatic --no-input
