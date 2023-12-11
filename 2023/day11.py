import doctest
import itertools
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)


def manhattan(a, b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def main():
    grid = dict()

    with open('day11_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                if c != ".":
                    grid[Point(x, y)] = c
            max_x = x
        max_y = y

    expand_rows = []
    expand_cols = []
    for y in range(max_y + 1):
        if all(Point(x, y) not in grid for x in range(max_x + 1)):
            expand_rows.append(y)
    for x in range(max_x + 1):
        if all(Point(x, y) not in grid for y in range(max_y + 1)):
            expand_cols.append(x)

    print(max_x, max_y)
    print(expand_rows, expand_cols)

    expanded_grid = dict()
    for point, value in grid.items():
        new_x = point.x + sum(1 for c in expand_cols if c < point.x)
        new_y = point.y + sum(1 for r in expand_rows if r < point.y)
        expanded_grid[Point(new_x, new_y)] = value

    part1 = 0
    for a, b in itertools.combinations(expanded_grid, 2):
        distance = manhattan(a, b)
        # print(a, b, distance)
        part1 += distance

    print(f"Part 1: {part1}")


if __name__ == "__main__":
    doctest.testmod()
    main()
