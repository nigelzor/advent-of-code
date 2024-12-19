import doctest
from functools import lru_cache


@lru_cache(2048)
def pattern_possibilities(pattern, available):
    """
    >>> pattern_possibilities("bb", ("b", "bb"))
    2
    """
    if pattern == "":
        return 1
    return sum(
        pattern_possibilities(pattern[len(a) :], available)
        for a in available
        if pattern.startswith(a)
    )


def main():
    with open("day19_input.txt") as f:
        lines = iter(line.strip() for line in f)

        available = tuple(next(lines).split(", "))
        next(lines)
        desired = list(lines)

    part1 = 0
    part2 = 0
    for pattern in desired:
        possibilities = pattern_possibilities(pattern, available)
        if possibilities:
            part1 += 1
            part2 += possibilities

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
