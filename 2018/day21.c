#include <stdio.h>

int main() {
    int r0 = 0, r1 = 0, r2 = 0, r3 = 0, r4 = 0, r5 = 0;
    while (1) {
        printf("regs: %i %i %i %i %i %i\n", r0, r1, r2, r3, r4, r5);
        switch (r1) {
        case 0: r5 = 123; break;
        case 1: r5 = r5 & 456; break;
        case 2: r5 = r5 == 72; break;
        case 3: r1 = r5 + r1; break;
        case 4: r1 = 0; break;
        case 5: r5 = 0; break;
        case 6: r4 = r5 | 65536; break;
        case 7: r5 = 13431073; break;
        case 8: r3 = r4 & 255; break;
        case 9: r5 = r5 + r3; break;
        case 10: r5 = r5 & 16777215; break;
        case 11: r5 = r5 * 65899; break;
        case 12: r5 = r5 & 16777215; break;
        case 13: r3 = 256 > r4; break;
        case 14: r1 = r3 + r1; break;
        case 15: r1 = r1 + 1; break;
        case 16: r1 = 27; break;
        case 17: r3 = 0; break;
        case 18: r2 = r3 + 1; break;
        case 19: r2 = r2 * 256; break;
        case 20: r2 = r2 > r4; break;
        case 21: r1 = r2 + r1; break;
        case 22: r1 = r1 + 1; break;
        case 23: r1 = 25; break;
        case 24: r3 = r3 + 1; break;
        case 25: r1 = 17; break;
        case 26: r4 = r3; break;
        case 27: r1 = 7; break;
        case 28: r3 = r5 == r0; break;
        case 29: r1 = r3 + r1; break;
        case 30: r1 = 5; break;
        default:
            printf("r0 = %i\n", r0);
            return 0;
        }
        r1++;
    }
}
