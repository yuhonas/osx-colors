setup: Pipfile Pipfile.lock
	 	pip install --quiet pipenv --upgrade
		pipenv install --dev

lint:
		pipenv run pylint ./src
		pipenv run black ./src --check --line-length 110

reformat:
		pipenv run black ./src --line-length 110

test: lint
		python -m unittest

release:
		pip install --quiet build --upgrade
		python -m build
