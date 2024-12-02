import doctest
from itertools import pairwise, combinations


def main():
    part1 = 0
    part2 = 0

    def safe(levels):
        changes = set(a - b for a, b in pairwise(levels))
        return changes <= {1, 2, 3} or changes <= {-1, -2, -3}

    with open("day2_input.txt") as f:
        for line in f:
            levels = [int(x) for x in line.split()]
            if safe(levels):
                part1 += 1
                part2 += 1
            elif any(safe(c) for c in combinations(levels, len(levels) - 1)):
                part2 += 1

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
