.PHONY: build, test, run-sims

IMAGE_NAME ?= 'planet_resource'
BUILD_ID ?= 'local'
BUILD_TAG ?= '$(IMAGE_NAME):$(BUILD_ID)'
DEV_TAG ?= 'dev/$(BUILD_TAG)'
TEST_TAG ?= 'test/$(BUILD_TAG)'
SIM_TAG ?= 'sim/$(BUILD_TAG)'
TEST_FILE ?= '*'
SIM_FILE ?= '*'

build:
	@set -eux;
		docker build --target=build --tag=$(BUILD_TAG) \
		--file="./Dockerfile" .

dev-build:
	@set -eux;
		docker build --target=dev --tag=$(DEV_TAG) \
		--file="./Dockerfile" .

test-build:
	@set -eux;
		docker build --target=test --tag=$(TEST_TAG) \
		--file="./Dockerfile" .

sim-build:
	@set -eux;
		docker build --target=sim --tag=$(SIM_TAG) \
		--build-arg SIM_FILE=$(SIM_FILE) \
		--file="./Dockerfile" .

dev: dev-build
	@docker run -it --rm $(DEV_TAG);

test: test-build
	@docker run --rm $(TEST_TAG);

sim: sim-build
	@docker run --rm $(SIM_TAG);

