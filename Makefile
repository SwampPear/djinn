IMAGE = djinn
CONTAINER = djinn-container

build:
	docker build -t $(IMAGE) .

run:
	docker stop $(CONTAINER)
	docker rm $(CONTAINER)
	docker run --name $(CONTAINER) -d -p 8000:8000 $(IMAGE)

test:
	echo "TODO: implement testing"