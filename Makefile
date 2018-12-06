CFLAGS=-fsanitize=address

.PHONY: all
all: venv day5

venv:
	virtualenv -p python3 venv
