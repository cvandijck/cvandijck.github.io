.PHONY: build

ifeq ($(OS), Windows_NT)
	MAKE_OS := Windows
else
	MAKE_OS := Linux
endif

PYTHON_VERSION = 3.11
VENV_NAME = .venv

BUILD_DIR = ./build

ifeq ($(MAKE_OS), Windows)
	CREATE_ENV_CMD=py -$(PYTHON_VERSION) -m venv $(VENV_NAME)
	PYTHON=$(VENV_NAME)\Scripts\python
	ACTIVATE=$(VENV_NAME)\Scripts\activate
	NPM=npm
else
	CREATE_ENV_CMD=python$(PYTHON_VERSION) -m venv $(VENV_NAME)
	PYTHON=$(VENV_NAME)/bin/python
	ACTIVATE=source $(VENV_NAME)/bin/activate
	NPM=npm
endif

RUN_MODULE = $(PYTHON) -m
PIP = $(RUN_MODULE) pip

install: create-env install-project install-pre-commit

create-env:
	$(info MAKE: Initializing environment in .venv ...)
	$(CREATE_ENV_CMD)
	$(PIP) install --upgrade "pip>=24" wheel

install-project:
	$(info MAKE: Installing project ...)
	$(PIP) install -r requirements.txt
	$(NPM) install

pre-commit:
	$(info MAKE: Pre-commit hooks check over all files...)
	$(RUN_MODULE) pre_commit run --all-files

build:
	$(info MAKE: render templates and build css)
	$(PYTHON) src/render_templates.py
	$(NPM) run build

show:
	explorer index.html
