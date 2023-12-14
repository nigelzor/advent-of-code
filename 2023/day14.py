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

    def tilt_n():
        for y in range(1, max_y + 1):
            for x in range(0, max_x + 1):
                if grid.get(Point(x, y)) == 'O':
                    north = y - 1
                    while north >= 0 and grid.get(Point(x, north)) is None:
                        grid[Point(x, north)] = 'O'
                        del grid[Point(x, north + 1)]
                        north -= 1

    def tilt_w():
        for x in range(1, max_x + 1):
            for y in range(0, max_y + 1):
                if grid.get(Point(x, y)) == 'O':
                    west = x - 1
                    while west >= 0 and grid.get(Point(west, y)) is None:
                        grid[Point(west, y)] = 'O'
                        del grid[Point(west + 1, y)]
                        west -= 1

    def tilt_s():
        for y in reversed(range(0, max_y)):
            for x in range(0, max_x + 1):
                if grid.get(Point(x, y)) == 'O':
                    south = y + 1
                    while south <= max_y and grid.get(Point(x, south)) is None:
                        grid[Point(x, south)] = 'O'
                        del grid[Point(x, south - 1)]
                        south += 1

    def tilt_e():
        for x in reversed(range(0, max_x)):
            for y in range(0, max_y + 1):
                if grid.get(Point(x, y)) == 'O':
                    east = x + 1
                    while east <= max_x and grid.get(Point(east, y)) is None:
                        grid[Point(east, y)] = 'O'
                        del grid[Point(east - 1, y)]
                        east += 1

    def load():
        total = 0
        for y in range(0, max_y + 1):
            weight = max_y - y + 1
            count = sum(1 for x in range(0, max_x + 1) if grid.get(Point(x, y)) == 'O')
            total += weight * count
        return total

    load_history = []
    for i in range(max_x + max_y):
        tilt_n()
        if i == 0:
            print(f"Part 1: {load()}")
        tilt_w()
        tilt_s()
        tilt_e()
        load_history.append(load())

    for cycle_length in range(1, (max_x + max_y) // 2):
        pattern = load_history[-cycle_length:]
        if load_history[-2 * cycle_length:-cycle_length] == pattern:
            # print(f"pattern with length {cycle_length}")
            target = 1000000000 % cycle_length
            for i in range(len(load_history) - 1, -1, -1):
                if (i + 1) % cycle_length == target:
                    print(f"Part 2: {load_history[i]}")
                    break


if __name__ == "__main__":
    doctest.testmod()
    main()
