CPPFLAGS += -O3 -fsanitize=address

.PHONY: all
all: .libs 2018/day5 2018/day19 2018/day21

venv:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip setuptools wheel

requirements.txt: requirements-to-freeze.txt venv
	venv/bin/pip install -r requirements-to-freeze.txt --upgrade
	venv/bin/pip freeze -r requirements-to-freeze.txt > requirements.txt

.libs: venv requirements.txt
	venv/bin/pip install -r requirements.txt
	touch .libs

.PHONY: lint
lint:
	venv/bin/flake8 --ignore=E501 2020/*.py
