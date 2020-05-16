.PHONY: activate, deactivate, install, test, run-sims

TESTFILE="*"
SIM="*"
PYENV_VERSION="3.8.2"
PYTHON="$(HOME)/.pyenv/versions/game-${PYENV_VERSION}/bin/python"
PIP="$(HOME)/.pyenv/versions/game-${PYENV_VERSION}/bin/pip3"

install:
	@./install.sh $(PYENV_VERSION);

build:
	@set -eux;
		$(PIP) install --upgrade pip; \
		$(PIP) install -e ./game;

test:
	@nosetests --verbose ./game/tests/`echo $(TESTFILE)`;

run-sims: build
	$(PYTHON) ./simulations/run_sims.py $(SIM)
