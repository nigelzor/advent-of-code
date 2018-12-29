#include <stdio.h>

int main() {
    int r0 = 3115806, r4 = 0, r5 = 0;
    r5 = 123;
    while (1) {
        r5 = r5 & 456;
        r5 = r5 == 72;
        if (r5) {
            break;
        }
    }
    r5 = 0;
    while (1) {
        r4 = r5 | 65536;
        r5 = 13431073;
        while (1) {
            r5 = r5 + (r4 & 255);
            r5 = r5 & 16777215;
            r5 = r5 * 65899;
            r5 = r5 & 16777215;
            if (256 > r4) {
                break;
            }
            r4 = r4 / 256;
        }
        printf("checking %i == %i\n", r5, r0);
        if (r5 == r0) {
            break;
        }
    }
    puts("exiting");
    return 0;
}
