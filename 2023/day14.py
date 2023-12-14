import doctest
from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)


def main():
    grid = dict()

    def bounds(g):
        minx = 0
        maxx = max(c.x for c in g.keys())
        miny = 0
        maxy = max(c.y for c in g.keys())
        return minx, maxx, miny, maxy

    def print_grid(g):
        minx, maxx, miny, maxy = bounds(g)
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                print(g.get(Point(x, y), '.'), end='')
            print('')

    with open('day14_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                if c != '.':
                    grid[Point(x, y)] = c

    # print_grid(grid)

    max_x = max(c.x for c in grid.keys())
    max_y = max(c.y for c in grid.keys())

    for y in range(1, max_y + 1):
        for x in range(0, max_x + 1):
            if grid.get(Point(x, y)) == 'O':
                above = y - 1
                while above >= 0 and grid.get(Point(x, above)) is None:
                    grid[Point(x, above)] = 'O'
                    del grid[Point(x, above + 1)]
                    above -= 1

    print_grid(grid)

    part1 = 0
    for y in range(0, max_y + 1):
        weight = max_y - y + 1
        count = sum(1 for x in range(0, max_x + 1) if grid.get(Point(x, y)) == 'O')
        part1 += weight * count

    print(f"Part 1: {part1}")


if __name__ == "__main__":
    doctest.testmod()
    main()
