run:
	python main.py

init:
	pip install -r requirements.txt

local:
	source env/bin/activate

log:
	python -m pip freeze > requirements.txt

.PHONY: run init local log