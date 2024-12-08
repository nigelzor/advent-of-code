import doctest
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)


def main():
    frequencies = defaultdict(set)
    max_x = 0
    max_y = 0

    with open("day8_input.txt") as f:
        for y, line in enumerate(f):
            max_y = max(max_y, y)
            for x, c in enumerate(line.strip()):
                max_x = max(max_x, x)
                if c == ".":
                    continue
                frequencies[c].add(Point(x, y))

    def in_bounds(point):
        return 0 <= point.x <= max_x and 0 <= point.y <= max_y

    antinodes = set()
    for frequency, nodes in frequencies.items():
        for a, b in combinations(nodes, 2):
            l = a + (a - b)
            r = b + (b - a)
            if in_bounds(l):
                antinodes.add(l)
            if in_bounds(r):
                antinodes.add(r)

    print(f"part 1: {len(antinodes)}")

    antinodes = set()
    for frequency, nodes in frequencies.items():
        for a, b in combinations(nodes, 2):
            angle = a - b
            p = a
            while in_bounds(p):
                antinodes.add(p)
                p += angle
            p = a
            while in_bounds(p):
                antinodes.add(p)
                p -= angle

    print(f"part 2: {len(antinodes)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
