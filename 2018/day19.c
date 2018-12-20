#include <stdio.h>

int main() {
    int r0 = 0, r1 = 0, r2 = 0, r3 = 0, r4 = 0, r5 = 0;

    r2 = (19 * 4 * 11) + ((8 * 22) + 18); // 1030
    if (r0) {
        r2 = r2 + (30 * (29 + (27 * 28)) * 14 * 32); // 10550400 + 1030
        r0 = 0;
    }
    r4 = 1;
label_2:
    r3 = 1;
label_3:
    if (r4 * r3 == r2) {
        r0 = r4 + r0;
    }
    r3++;
    if (!(r3 > r2)) {
        goto label_3;
    }
    r4++;
    if (r4 > r2) {
        printf("r0 = %i\n", r0);
        return 0;
    } else {
        goto label_2;
    }
}