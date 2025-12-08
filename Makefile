CPPFLAGS += -O3 -fsanitize=address

.PHONY: all
all: .libs 2018/day5 2018/day19 2018/day21

venv:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip setuptools wheel pip-tools

requirements.txt: requirements.in venv
	venv/bin/pip-compile

.libs: venv requirements.txt
	venv/bin/pip-sync requirements.txt
	touch .libs

.PHONY: lint
lint:
	venv/bin/ruff check --ignore E741 2023 2024 2025
	venv/bin/ruff format 2024 2025
