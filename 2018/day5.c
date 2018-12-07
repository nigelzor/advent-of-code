#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <fcntl.h>

int react(char skip) {
	struct stat sb;
	int fd = open("day5.txt", O_RDONLY);
	fstat(fd, &sb);

	char *buf = mmap(NULL, sb.st_size, PROT_WRITE, MAP_PRIVATE, fd, 0);
	int pos = -1;
	for (int i = 0; i < sb.st_size; i++) {
		char c = buf[i];
		if (skip && (c == skip || c - 32 == skip)) {
			continue;
		}
		if (pos >= 0 && (buf[pos] == (c ^ ' '))) {
			pos--;
		} else {
			pos++;
			buf[pos] = c;
		}
	}
	buf[pos] = 0;
	munmap(buf, sb.st_size);
	return pos;
}

int main() {
	int len = react(0);
	printf("length: %i\n", len);
	char min_s;
	int min = INT_MAX;
	for (char s = 'A'; s <= 'Z'; s++) {
		len = react(s);
		if (len < min) {
			min = len;
			min_s = s;
		}
	}
	printf("length when skipping %c: %i\n", min_s, min);
}
