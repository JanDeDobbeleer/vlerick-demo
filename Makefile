.PHONY:
	test
	lint
	dependencies
	ci

ci: lint static test

dependencies:
	python3 -m pip install -r requirements.txt

test:
	pytest --cov=. --cov-config=setup.cfg --cov-fail-under=100

lint:
	flake8 .

static:
	mypy .
