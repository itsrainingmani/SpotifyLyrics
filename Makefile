.PHONY: help init test run lint

TEST_PATH=./tests

.DEFAULT: help
help:
	@echo "make init"
	@echo "    Setup environment from Pipfile using pipenv"
	@echo "make test"
	@echo "    run tests"
	@echo "make run"
	@echo "    run project"
	@echo "make lint"
	@echo "    lint the source files using flake8"

init:
	pipenv install

test:
	pipenv run python -m pytest --verbose --color=yes $(TEST_PATH)

run:
	pipenv run python lyrics/app.py

lint:
	pipenv run flake8 pal/*