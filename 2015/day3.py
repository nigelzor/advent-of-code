import doctest
from collections import defaultdict


def part1(instructions):
    """
    >>> part1(">")
    2
    >>> part1("^>v<")
    4
    >>> part1("^v^v^v^v^v")
    2
    """
    houses = defaultdict(int)
    deliver(houses, instructions)
    return len(houses)


def part2(instructions):
    """
    >>> part2("^v")
    3
    >>> part2("^>v<")
    3
    >>> part2("^v^v^v^v^v")
    11
    """
    houses = defaultdict(int)
    deliver(houses, (x for i, x in enumerate(instructions) if i % 2 == 0))
    deliver(houses, (x for i, x in enumerate(instructions) if i % 2 == 1))
    return len(houses)


def deliver(houses, instructions):
    x = 0
    y = 0
    houses[(x, y)] += 1
    for i in instructions:
        if i == '>':
            x += 1
        elif i == '<':
            x -= 1
        elif i == '^':
            y += 1
        elif i == 'v':
            y -= 1
        houses[(x, y)] += 1


def main():
    with open('day3_input.txt') as f:
        instructions = f.readlines()[0]

    print(part1(instructions))
    print(part2(instructions))


if __name__ == "__main__":
    doctest.testmod()
    main()
