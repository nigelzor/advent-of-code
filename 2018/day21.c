#include <stdio.h>

int main() {
    int r0 = 3115806, r1 = 0, r2 = 0, r3 = 0, r4 = 0, r5 = 0;
    while (1) {
        printf("regs: %i %i %i %i %i %i\n", r0, r1, r2, r3, r4, r5);
        switch (r1) {
        case 0:
            r5 = 123;
        case 1: // <
            r5 = r5 & 456;
            r5 = r5 == 72;
            r1 = r5 + 4;
            break;
        case 4: // <
            r1 = 1;
            break;
        case 5: // <
            r5 = 0;
            r4 = r5 | 65536;
            r5 = 13431073;
        case 8: // <
            r3 = r4 & 255;
            r5 = r5 + r3;
            r5 = r5 & 16777215;
            r5 = r5 * 65899;
            r5 = r5 & 16777215;
            r3 = 256 > r4;
            r1 = r3 + 15;
            break;
        case 15: // <
            r1 = 17;
            break;
        case 16: // <
            r1 = 28;
            break;
        case 17: // <
            r3 = 0;
        case 18: // <
            r2 = r3 + 1;
            r2 = r2 * 256;
            r2 = r2 > r4;
            r1 = r2 + 22;
            break;
        case 22: // <
            r1 = 24;
            break;
        case 23: // <
            r1 = 26;
            break;
        case 24: // <
            r3 = r3 + 1;
            r1 = 18;
            break;
        case 26: // <
            r4 = r3;
            r1 = 8;
            break;
        case 28: // <
            r3 = r5 == r0;
            r1 = r3 + 30;
            break;
        case 30: // <
            r1 = 6;
            break;
        default:
            puts("exiting");
            return 0;
        }
    }
}
