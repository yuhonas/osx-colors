setup: Pipfile Pipfile.lock
	 	pip install --quiet pipenv
		pipenv install --dev

lint:
		pipenv run pylint ./src

test: lint
		python -m unittest
