#include <stdio.h>

int main() {
    int r0 = 1, r1 = 0, r2 = 0, r3 = 0, r4 = 0, r5 = 0;
    while (1) {
        switch (r5) {
        case 0: r5 = r5 + 16; break;
        case 1: r4 = 1; break;
        case 2: r3 = 1; break;
        case 3: r1 = r4 * r3; break;
        case 4: r1 = r1 == r2; break;
        case 5: r5 = r1 + r5; break;
        case 6: r5 = r5 + 1; break;
        case 7: r0 = r4 + r0; break;
        case 8: r3 = r3 + 1; break;
        case 9: r1 = r3 > r2; break;
        case 10: r5 = r5 + r1; break;
        case 11: r5 = 2; break;
        case 12: r4 = r4 + 1; break;
        case 13: r1 = r4 > r2; break;
        case 14: r5 = r1 + r5; break;
        case 15: r5 = 1; break;
        case 16: r5 = r5 * r5; break;
        case 17: r2 = r2 + 2; break;
        case 18: r2 = r2 * r2; break;
        case 19: r2 = r5 * r2; break;
        case 20: r2 = r2 * 11; break;
        case 21: r1 = r1 + 8; break;
        case 22: r1 = r1 * r5; break;
        case 23: r1 = r1 + 18; break;
        case 24: r2 = r2 + r1; break;
        case 25: r5 = r5 + r0; break;
        case 26: r5 = 0; break;
        case 27: r1 = r5; break;
        case 28: r1 = r1 * r5; break;
        case 29: r1 = r5 + r1; break;
        case 30: r1 = r5 * r1; break;
        case 31: r1 = r1 * 14; break;
        case 32: r1 = r1 * r5; break;
        case 33: r2 = r2 + r1; break;
        case 34: r0 = 0; break;
        case 35: r5 = 0; break;
        default:
            printf("r0 = %i\n", r0);
            return 0;
        }
        r5++;
    }
}