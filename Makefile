.PHONY: test, run-sims

test:
	@python3.7 -m "nose" --verbose ./game/tests/*

run-sims:
	@python3.7 ./simulations/*.py
