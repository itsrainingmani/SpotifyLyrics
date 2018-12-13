.PHONY: help init test run lint

TEST_PATH=./tests

.DEFAULT: help
help:
	@echo "make init  -  Setup environment from Pipfile using pipenv"
	@echo "make test  -  Run tests"
	@echo "make run   -  Run project"
	@echo "make lint  -  Lint the source files using flake8"
	@echo "make clean -  Clean the lyrics cache folder"

init:
	pipenv install

test:
	pipenv run python -m pytest --verbose --color=yes $(TEST_PATH)

run:
	pipenv run python lyrics/app.py

lint:
	pipenv run flake8