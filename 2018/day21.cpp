#include <cstdio>
#include <set>

int main() {
    std::set<int> seen;
    int previous = 0;
    int r4 = 0, r5 = 0;
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
        if (seen.empty()) {
            printf("first: %i\n", r5);
        }
        if (!seen.insert(r5).second) {
            printf("last: %i\n", previous);
            printf("duplicate: %i\n", r5);
            break;
        }
        previous = r5;
    }
    puts("exiting");
    return 0;
}
