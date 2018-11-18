.PHONY: install
install:
	python3 setup.py install

.PHONY: server
server:
	pipenv run python -m mock_server

.PHONY: deps
deps:
	pipenv install

.PHONY: run
run:
	sudo pipenv run python -m voctokey
