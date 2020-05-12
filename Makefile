.PHONY: install, test, run-sims

install:
	@pip3.7 install -e ./game

TESTFILE="*"
test:
	@python3.7 -m "nose" --verbose ./game/tests/`echo $(TESTFILE)`

SIMFILES="*"
run-sims:
	@python3.7 ./simulations/`echo $(SIMFILES)`
