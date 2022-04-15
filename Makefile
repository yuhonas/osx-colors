setup: Pipfile Pipfile.lock
	 	pip install --quiet pipenv --upgrade
		pipenv install --dev

lint:
		pipenv run pylint ./src

test: lint
		python -m unittest

release:
		pip install --quiet build --upgrade
		python -m build
