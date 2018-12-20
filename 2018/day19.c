#include <stdio.h>

int main() {
    int r0 = 0, r1 = 0, r2 = 0, r3 = 0, r4 = 0, r5 = 0;
    while (1) {
        switch (r5) {
        case 0:
            r5 = 17; // .
            break;
        case 1: // in from 35
            r4 = 1;
            r5++;
        case 2: // in from 15
            r3 = 1;
            r5++;
        case 3: // in from 11
            r1 = r4 * r3;
            r5++;
        case 4:
            r1 = r1 == r2;
            r5++;
        case 5:
            r5 = r1 + 6;
            break;
        case 6: // in from 5
            r5 = 8;
            break;
        case 7: // in from 5
            r0 = r4 + r0;
            r5++;
        case 8: // in from 6
            r3 = r3 + 1;
            r5++;
        case 9:
            r1 = r3 > r2;
            r5++;
        case 10:
            r5 = 11 + r1;
            break;
        case 11: // in from 10
            r5 = 3;
            break;
        case 12: // in from 10
            r4 = r4 + 1;
            r5++;
        case 13:
            r1 = r4 > r2;
            r5++;
        case 14:
            r5 = 15 + r1;
            break;
        case 15: // in from 14
            r5 = 2;
            break;
        case 16: // in from 14
            r5 = 257;
            break;
        case 17: // in from 0
            r2 = r2 + 2;
            r5++;
        case 18:
            r2 = r2 * r2;
            r5++;
        case 19:
            r2 = 19 * r2;
            r5++;
        case 20:
            r2 = r2 * 11;
            r5++;
        case 21:
            r1 = r1 + 8;
            r5++;
        case 22:
            r1 = r1 * 22;
            r5++;
        case 23:
            r1 = r1 + 18;
            r5++;
        case 24:
            r2 = r2 + r1;
            r5++;
        case 25:
            r5 = 26 + r0;
            break;
        case 26: // in from 25 (to end)
            r5 = 1;
            break;
        case 27: // in from 25 (to end)
            r1 = 27;
            r5++;
        case 28:
            r1 = r1 * 28;
            r5++;
        case 29:
            r1 = 29 + r1;
            r5++;
        case 30:
            r1 = 30 * r1;
            r5++;
        case 31:
            r1 = r1 * 14;
            r5++;
        case 32:
            r1 = r1 * 32;
            r5++;
        case 33:
            r2 = r2 + r1;
            r5++;
        case 34:
            r0 = 0;
            r5++;
        case 35:
            r5 = 1;
            break;
        default:
            printf("r0 = %i\n", r0);
            return 0;
        }
    }
}