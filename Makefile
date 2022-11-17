# -*- MakeFile -*-
DOCKER_IMAGE=manim:dev

all: build manim

.PHONY: clean

build:
	@echo "Building Docker image..."
	docker build -t $(DOCKER_IMAGE) .

manim:
	@echo "Running shell in Docker container..."
	docker run -it --rm -v python_source:/opt/src $(DOCKER_IMAGE)

clean:
	@echo "Removing all manim images..."
	docker image prune -f --filter label=stage=manim_build
