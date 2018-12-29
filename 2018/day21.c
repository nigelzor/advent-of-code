#include <stdio.h>

int main() {
    int r0 = 3115806, r1 = 0, r2 = 0, r3 = 0, r4 = 0, r5 = 0;
    printf("regs: %i %i %i %i %i %i\n", r0, r1, r2, r3, r4, r5);
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
            r3 = r4 & 255;
            r5 = r5 + r3;
            r5 = r5 & 16777215;
            r5 = r5 * 65899;
            r5 = r5 & 16777215;
            r3 = 256 > r4;
            if (r3) {
                break;
            }
            r3 = 0;
            while (1) {
                r2 = r3 + 1;
                r2 = r2 * 256;
                r2 = r2 > r4;
                if (r2) {
                    r4 = r3;
                    break;
                }
                r3 = r3 + 1;
            }
        }
        r3 = r5 == r0;
        if (r3) {
            break;
        }
    }
    printf("regs: %i %i %i %i %i %i\n", r0, r1, r2, r3, r4, r5);
    puts("exiting");
    return 0;
}
