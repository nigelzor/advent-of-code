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


def connects_north(a):
    return a == "S" or a == "|" or a == "L" or a == "J"


def connects_south(a):
    return a == "S" or a == "|" or a == "7" or a == "F"


def connects_west(a):
    return a == "S" or a == "-" or a == "J" or a == "7"


def connects_east(a):
    return a == "S" or a == "-" or a == "L" or a == "F"


def main():
    grids = []
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
            print(f"{y}: ", end='')
            for x in range(minx, maxx + 1):
                print(g.get(Point(x, y), '.'), end='')
            print('')

    with open('day13_input.txt') as f:
        y = 0
        for line in f:
            line = line.strip()
            if not line:
                y = 0
                grids.append(grid)
                grid = dict()
            else:
                for x, c in enumerate(line.strip()):
                    grid[Point(x, y)] = c
                y += 1
    grids.append(grid)

    part1 = 0
    for i, grid in enumerate(grids):
        max_x = max(c.x for c in grid.keys())
        max_y = max(c.y for c in grid.keys())
        print(f"Grid {i} {max_x}x{max_y}")
        print_grid(grid)

        def equal_rows(a, b):
            for x in range(0, max_x + 1):
                if grid[Point(x, a)] != grid[Point(x, b)]:
                    return False
            return True

        def equal_cols(a, b):
            for y in range(0, max_y + 1):
                if grid[Point(a, y)] != grid[Point(b, y)]:
                    return False
            return True

        def is_vertical_reflection(row):
            # print(f"testing between rows {row} and {row+1}")
            rows_to_check = min(row + 1, max_y - row)
            for y in range(0, rows_to_check):
                if not equal_rows(row - y, row + y + 1):
                    return False
            return True

        def is_horizontal_reflection(col):
            # print(f"testing between cols {col} and {col+1}")
            cols_to_check = min(col + 1, max_x - col)
            for x in range(0, cols_to_check):
                if not equal_cols(col - x, col + x + 1):
                    return False
            return True

        vertical_reflection = next((row for row in range(0, max_y) if is_vertical_reflection(row)), -1)
        horizontal_reflection = next((col for col in range(0, max_x) if is_horizontal_reflection(col)), -1)
        print(f"vr: {vertical_reflection}, hr: {horizontal_reflection}")
        part1 += 100 * (vertical_reflection + 1) + (horizontal_reflection + 1)

    print(f"Part1: {part1}")


if __name__ == "__main__":
    doctest.testmod()
    main()
