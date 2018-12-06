#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>

int react(char skip) {
	int pos = -1;
	int bsz = 1024;
	char *buf = malloc(bsz * sizeof(char));
	FILE *f = fopen("day5.txt", "rb");
	int c;
	if (f) {
		while ((c = getc(f)) != EOF) {
			if (skip && (c == skip || c - 32 == skip)) {
				continue;
			}
			if (pos >= 0 && ((buf[pos] == (c - 32)) || (buf[pos] == (c + 32)))) {
				pos--;
			} else {
				pos += 1;
				if (pos >= bsz) {
					bsz *= 2;
					buf = realloc(buf, bsz * sizeof(char));
				}
				buf[pos] = c;
			}
		}
	}
	buf[pos] = 0;
	// puts(buf);
	// printf("skipping %c, length: %i\n", skip, pos);
	fclose(f);
	free(buf);
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
