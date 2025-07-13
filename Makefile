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