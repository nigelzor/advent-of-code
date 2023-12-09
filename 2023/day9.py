import doctest
import itertools
import re


def main():
    whitespace = re.compile(" +")

    lines = []
    with open('day9_input.txt') as f:
        for line in f:
            lines.append([int(x) for x in whitespace.split(line.strip())])

    part1 = sum(extrapolate_end(line) for line in lines)
    print(f"Part 1: {part1}")
    part2 = sum(extrapolate_start(line) for line in lines)
    print(f"Part 2: {part2}")


def extrapolate_end(ns):
    if all(n == 0 for n in ns):
        return 0
    return ns[-1] + extrapolate_end(list(differences(ns)))


def extrapolate_start(ns):
    if all(n == 0 for n in ns):
        return 0
    return ns[0] - extrapolate_start(list(differences(ns)))


def differences(ns):
    for (a, b) in itertools.pairwise(ns):
        yield b - a


if __name__ == "__main__":
    doctest.testmod()
    main()
