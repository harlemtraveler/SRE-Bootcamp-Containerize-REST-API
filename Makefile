run:
	FLASK_APP=run.py flask run

migrate:
	FLASK_APP=run.py flask db migrate

upgrade:
	FLASK_APP=run.py flask db upgrade

test:
	pytest tests/

lint:
	flake8 app/ tests/

DOCKER_IMAGE_NAME=student-api
DOCKER_VERSION=0.1.0

docker-build:
	docker build -t $(DOCKER_IMAGE_NAME):$(DOCKER_VERSION)

docker-shell:
	docker run -it --rm --env-file .env $(DOCKER_IMAGE_NAME):$(DOCKER_VERSION) sh