.PHONY: install
install:
	python3 setup.py install

.PHONY: deps
deps:
	pipenv install

.PHONY: run
run:
	sudo pipenv run python -m voctokey
