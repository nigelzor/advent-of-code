CFLAGS=-fsanitize=address

.PHONY: all
all: venv 2018/day5

venv:
	virtualenv -p python3 venv
