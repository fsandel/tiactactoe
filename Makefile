NAME = Test

init:
	pip install -r requirements.txt

test:
	py.test tests

run:
	python test.py

local:
	source env/bin/activate

log:
	python -m pip freeze > requirements.txt

.PHONY: init test