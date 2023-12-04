import doctest
import re
from collections import defaultdict


def main():
    whitespace = re.compile(" +")

    part1 = 0

    copies = defaultdict(lambda: 1)

    with open('day4_input.txt') as f:
        for n, line in enumerate(f, start=1):
            [left, right] = line.split(":")[1].split("|")
            left = set(int(x) for x in whitespace.split(left.strip()))
            right = set(int(x) for x in whitespace.split(right.strip()))

            matches = len(left & right)
            # print(f"{n}, {matches}, *{copies[n]}")

            if matches > 0:
                part1 += pow(2, matches - 1)
                if copies[n]:
                    for x in range(matches):
                        # print(f"adding {copies[n]} to {n+x+1}")
                        copies[n + x + 1] += copies[n]
    part2 = sum(copies.values())

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
