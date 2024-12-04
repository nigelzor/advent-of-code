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

DIRECTIONS = (N, S, E, W, NE, NW, SE, SW)


def main():
    map = dict()

    def is_xmas(point, direction):
        if map.get(point) != "X":
            return False
        point += direction
        if map.get(point) != "M":
            return False
        point += direction
        if map.get(point) != "A":
            return False
        point += direction
        if map.get(point) != "S":
            return False
        return True

    def is_mas(point):
        return (
            (map.get(point) == "A")
            and (
                (map.get(point + NW) == "S" and map.get(point + SE) == "M")
                or (map.get(point + NW) == "M" and map.get(point + SE) == "S")
            )
            and (
                (map.get(point + NE) == "S" and map.get(point + SW) == "M")
                or (map.get(point + NE) == "M" and map.get(point + SW) == "S")
            )
        )

    part1 = 0
    part2 = 0

    with open("day4_input.txt") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line):
                map[Point(x, y)] = c

    max_x = max(p.x for p in map)
    max_y = max(p.y for p in map)

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            for direction in DIRECTIONS:
                if is_xmas(Point(x, y), direction):
                    part1 += 1
            if is_mas(Point(x, y)):
                part2 += 1

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
