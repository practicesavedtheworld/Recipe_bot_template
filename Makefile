.PHONY: tests run_as_script venv_init tests_poetry run_as_script_poetry install install_poetry default_recipes default_recipes_poetry

OS:=$(shell uname -s)


# Create venv
venv_init:
ifeq ($(OS),Windows)
	@python3 -m venv venv && \
	. \venv\Scripts\activate;
else
	@python3 -m venv venv && \
	source venv/bin/activate;
endif

# Remove venv
venv_clean:
	@rm -rf venv

# Classic install using pip. Before installing requirements runs venv_init
install: venv_init
	@pip install --upgrade pip && \
	pip install -r requirements.txt

install_poetry:
	@poetry update && \
	poetry install


tests: install
	pytest tests/ -v

tests_poetry: install_poetry
	poetry run pytest tests/ -v

# Run entrypoint without poetry
run_as_script: install
	python3 main.py

# Run entrypoint with poetry
run_as_script_poetry: install_poetry
	poetry run python3 main.py


############################################
# Default recipes push with/without poetry #
############################################
default_recipes: install
	python3 default_recipes_starter.py

default_recipes_poetry: install_poetry
	poetry run python3 default_recipes_starter.py
############################################

