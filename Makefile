.PHONY: install, test, run-sims

install:
	@pip3.7 install -e ./game

TESTFILE="*"
test:
	@python3.7 -m "nose" --verbose ./game/tests/`echo $(TESTFILE)`

SIM="*"
run-sims:
	@python3.7 ./simulations/run_sims.py $(SIM)
