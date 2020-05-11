.PHONY: test

test:
	@python3 -m "nose" --verbose ./game/tests/*
