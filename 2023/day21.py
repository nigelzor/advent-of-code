import doctest
from dataclasses import dataclass
from typing import Set


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)


def manhattan(a: Point, b: Point):
    return abs(a.x - b.x) + abs(a.y - b.y)


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)


def main():
    plots = set()
    with open('day21_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                if c == '.':
                    plots.add(Point(x, y))
                if c == 'S':
                    plots.add(Point(x, y))
                    start = Point(x, y)

    def step(occupied: Set[Point]):
        result = set()
        for o in occupied:
            for d in [N, E, S, W]:
                result.add(o + d)
        return result & plots

    occupied = {start}
    for _ in range(64):
        occupied = step(occupied)
    print(f'Part 1: {len(occupied)}')


if __name__ == "__main__":
    doctest.testmod()
    main()
