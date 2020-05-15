.PHONY: activate, deactivate, install, test, run-sims

TESTFILE="*"
SIM="*"
PYENV_VERSION="3.8.2"

install:
	@./install.sh $(PYENV_VERSION);

build:
	@pyenv local game-${PYENV_VERSION}; \
		pip install --upgrade pip; \
		pip install -e ./game;

test:
	@nosetests --verbose ./game/tests/`echo $(TESTFILE)`;

run-sims: build
	python ./simulations/run_sims.py $(SIM)
