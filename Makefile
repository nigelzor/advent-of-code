CFLAGS += -fsanitize=address
CPPFLAGS += -fsanitize=address

.PHONY: all
all: .libs 2018/day5 2018/day19 2018/day21

venv:
	virtualenv -p python3 venv

.libs: venv requirements.txt
	venv/bin/pip install -r requirements.txt
	touch .libs
