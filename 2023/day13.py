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
    part2 = 0
    for i, grid in enumerate(grids):
        max_x = max(c.x for c in grid.keys())
        max_y = max(c.y for c in grid.keys())
        # print(f"Grid {i} {max_x}x{max_y}")
        # print_grid(grid)

        def count_row_difference(a, b):
            difference = 0
            for x in range(0, max_x + 1):
                if grid[Point(x, a)] != grid[Point(x, b)]:
                    difference += 1
            return difference

        def count_col_difference(a, b):
            difference = 0
            for y in range(0, max_y + 1):
                if grid[Point(a, y)] != grid[Point(b, y)]:
                    difference += 1
            return difference

        def count_vertical_reflection_differences(row):
            # print(f"testing between rows {row} and {row+1}")
            rows_to_check = min(row + 1, max_y - row)
            return sum(count_row_difference(row - y, row + y + 1) for y in range(0, rows_to_check))

        def count_horizontal_reflection_differences(col):
            # print(f"testing between cols {col} and {col+1}")
            cols_to_check = min(col + 1, max_x - col)
            return sum(count_col_difference(col - x, col + x + 1) for x in range(0, cols_to_check))

        vertical_reflection_1 = next((row for row in range(0, max_y) if count_vertical_reflection_differences(row) == 0), -1)
        horizontal_reflection_1 = next((col for col in range(0, max_x) if count_horizontal_reflection_differences(col) == 0), -1)
        part1 += 100 * (vertical_reflection_1 + 1) + (horizontal_reflection_1 + 1)

        vertical_reflection_2 = next((row for row in range(0, max_y) if count_vertical_reflection_differences(row) == 1), -1)
        horizontal_reflection_2 = next((col for col in range(0, max_x) if count_horizontal_reflection_differences(col) == 1), -1)
        part2 += 100 * (vertical_reflection_2 + 1) + (horizontal_reflection_2 + 1)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
