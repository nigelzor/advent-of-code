import doctest
import itertools
from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
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
DIRECTIONS = {
    'N': N,
    'S': S,
    'E': E,
    'W': W,
    'NE': NE,
    'NW': NW,
    'SE': SE,
    'SW': SW,
}
ALL_DIRECTIONS = DIRECTIONS.values()
NORTHISH = (N, NE, NW)
SOUTHISH = (S, SE, SW)
WESTISH = (W, NW, SW)
EASTISH = (E, NE, SE)


def main():
    grid = dict()

    with open('day23_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line):
                if c == '#':
                    grid[Point(x, y)] = chr(len(grid) + ord('A'))

    def bounds():
        minx = min(c.x for c in grid.keys())
        maxx = max(c.x for c in grid.keys())
        miny = min(c.y for c in grid.keys())
        maxy = max(c.y for c in grid.keys())
        return minx, maxx, miny, maxy

    def print_grid():
        minx, maxx, miny, maxy = bounds()
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                print(grid.get(Point(x, y), '.'), end='')
            print('')

    def elf_in_directions(pos, directions):
        for d in directions:
            if pos + d in grid:
                return True
        return False

    def round(grid, order):
        idle = []
        proposed = defaultdict(list)
        for k, v in grid.items():
            if not elf_in_directions(k, ALL_DIRECTIONS):
                idle.append((k, v))
                continue
            for direction, check in order:
                if not elf_in_directions(k, check):
                    proposed[k + direction].append((k, v))
                    break
            else:
                idle.append((k, v))

        next_grid = dict()
        for k, v in idle:
            next_grid[k] = v
        for destination, elves in proposed.items():
            if len(elves) == 1:
                k, v = elves[0]
                next_grid[destination] = v
            else:
                for k, v in elves:
                    next_grid[k] = v

        assert(len(next_grid) == len(grid))
        return next_grid

    initial_directions = [(N, NORTHISH), (S, SOUTHISH), (W, WESTISH), (E, EASTISH)]
    order = itertools.cycle(initial_directions)

    def next_order():
        result = list(itertools.islice(order, 4))
        next(order)
        return result

    for r in range(10):
        # print(f'Round {r+1}')
        grid = round(grid, next_order())
        # print_grid()

    minx, maxx, miny, maxy = bounds()
    width = maxx - minx + 1
    height = maxy - miny + 1
    print(width * height - len(grid))  # 3925


if __name__ == "__main__":
    doctest.testmod()
    main()
