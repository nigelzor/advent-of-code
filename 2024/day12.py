import doctest
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)

DIRECTIONS = (N, S, E, W)


def cost(region):
    return len(region) * perimeter(region)


def perimeter(region):
    result = 0
    for c in region:
        for direction in DIRECTIONS:
            if c + direction not in region:
                result += 1
    return result


def main():
    farm = {}

    with open("day12_input.txt") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                farm[Point(x, y)] = c

    part1 = 0

    while farm:
        region = set()
        k, v = farm.popitem()
        pending = [k]
        while pending:
            k = pending.pop()
            region.add(k)
            for direction in DIRECTIONS:
                adjacent = k + direction
                if farm.get(adjacent) == v:
                    pending.append(adjacent)
                    del farm[adjacent]

        part1 += cost(region)

    print(f"part 1: {part1}")


if __name__ == "__main__":
    doctest.testmod()
    main()
