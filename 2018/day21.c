#include <stdio.h>

int main() {
    int r0 = 3115806, r1 = 0, r2 = 0, r3 = 0, r4 = 0, r5 = 0;
    printf("regs: %i %i %i %i %i %i\n", r0, r1, r2, r3, r4, r5);
    r5 = 123;
label_1:
    r5 = r5 & 456;
    r5 = r5 == 72;
    if (!r5) {
        goto label_1;
    }
    r5 = 0;
label_6:
    r4 = r5 | 65536;
    r5 = 13431073;
label_8:
    r3 = r4 & 255;
    r5 = r5 + r3;
    r5 = r5 & 16777215;
    r5 = r5 * 65899;
    r5 = r5 & 16777215;
    r3 = 256 > r4;
    if (r3) {
        goto label_28;
    }
    r3 = 0;
label_18:
    r2 = r3 + 1;
    r2 = r2 * 256;
    r2 = r2 > r4;
    if (r2) {
        goto label_26;
    }
    r3 = r3 + 1;
    goto label_18;
label_26:
    r4 = r3;
    goto label_8;
label_28:
    r3 = r5 == r0;
    if (!r3) {
        goto label_6;
    }
    printf("regs: %i %i %i %i %i %i\n", r0, r1, r2, r3, r4, r5);
    puts("exiting");
    return 0;
}
