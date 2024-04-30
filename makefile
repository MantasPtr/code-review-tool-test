.DEFAULT_GOAL := run-all

run-all: bandit mypy pylint flake8
install-all: install-bandit install-mypy install-pylint install-flake8

bandit:
	bandit -r examples/

install-bandit:
	pip install bandit

mypy:
	mypy examples/

install-mypy:
	pip install mypy


pylint:
	pylint examples/

install-pylint:
	pip install pylint


flake8:
	flake8 examples/

install-flake8:
	pip install flake8
