import doctest
from collections import defaultdict
from functools import lru_cache


def part1(lines):
    outlet = 0
    device = max(lines) + 3
    differences = defaultdict(int)

    current = outlet
    for v in lines:
        difference = v - current
        if difference > 3:
            raise Exception(f'difference too large ({difference})')
        differences[difference] += 1
        current = v

    difference = device - current
    differences[difference] += 1

    print(differences[1] * differences[3])


def paths_through_seq(seq):
    """
    >>> paths_through_seq([0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22])
    8
    >>> paths_through_seq([0, 1])
    1
    """
    @lru_cache(maxsize=None)
    def inner_paths(at):
        if at == len(seq) - 1:
            return 1
        paths = 0
        head = seq[at]
        for p in range(at + 1, at + 4):
            if p < len(seq) and seq[p] - head <= 3:
                paths += inner_paths(p)
        return paths
    return inner_paths(0)


def part2(lines):
    outlet = 0
    device = max(lines) + 3

    seq = [outlet] + lines + [device]
    print(paths_through_seq(seq))


def main():
    lines = []
    with open('day10_input.txt') as f:
        for line in f:
            lines.append(int(line))
    lines.sort()

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    doctest.testmod()
    main()
