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

NE = N + E
NW = N + W
SE = S + E
SW = S + W

DIRECTIONS = (N, S, E, W)


def price_1(region):
    return len(region) * perimeter(region)


def price_2(region):
    return len(region) * sides(region)


def perimeter(region):
    result = 0
    for c in region:
        for direction in DIRECTIONS:
            if c + direction not in region:
                result += 1
    return result


def sides(region):
    to_check = set()
    for c in region:
        to_check.add((c + NW, c + N, c + W, c))
        to_check.add((c + N, c + NE, c, c + E))
        to_check.add((c + W, c, c + SW, c + S))
        to_check.add((c, c + E, c + S, c + SE))

    return sum(count_corners(region, c) for c in to_check)


def count_corners(region, corner):
    """
    zero:
    AA
    AA
    .. A. AA .A
    AA A. .. .A
    ..
    ..
    one:
    .A A. AA AA
    AA AA A. .A
    A. .A .. ..
    .. .. .A A.
    two:
    .A A.
    A. .A
    """
    return {
        (False, True, True, True): 1,
        (True, False, True, True): 1,
        (True, True, False, True): 1,
        (True, True, True, False): 1,
        (True, False, False, False): 1,
        (False, True, False, False): 1,
        (False, False, True, False): 1,
        (False, False, False, True): 1,
        (False, True, True, False): 2,
        (True, False, False, True): 2,
    }.get(tuple(p in region for p in corner), 0)


def main():
    farm = {}

    with open("day12_input.txt") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                farm[Point(x, y)] = c

    part1 = 0
    part2 = 0

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

        part1 += price_1(region)
        part2 += price_2(region)

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
