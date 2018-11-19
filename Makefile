# Needed SHELL since I'm using zsh
SHELL := /bin/bash

.PHONY: install
install: ## Install the current version voctokey on your machine (might need sudo)
	python3 setup.py install

.PHONY: publish
publish: ## Publish new version on Pypi
	python setup.py sdist bdist_wheel
	twine upload dist/*

.PHONY: server
server: ## Run a dummy TCP server for testing
	pipenv run python -m mock_server

.PHONY: deps
deps: ## Install the project dependencies using pipenv
	pipenv install

.PHONY: run
run: ## Run voctokey and start listening for keyboard inputs.
	sudo pipenv run python -m voctokey

.PHONY: help
help: ## This help message
	@echo -e "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"
