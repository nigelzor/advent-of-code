import doctest
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


def connects_north(a):
    return a == "S" or a == "|" or a == "L" or a == "J"


def connects_south(a):
    return a == "S" or a == "|" or a == "7" or a == "F"


def connects_west(a):
    return a == "S" or a == "-" or a == "J" or a == "7"


def connects_east(a):
    return a == "S" or a == "-" or a == "L" or a == "F"


def main():
    grid = dict()
    distances = dict()
    start = None

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

    def print_grid_distances():
        minx, maxx, miny, maxy = bounds()
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                print(distances.get(Point(x, y), '.'), end='')
            print('')

    with open('day10_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                if c != ".":
                    grid[Point(x, y)] = c
                if c == "S":
                    start = Point(x, y)

    # print_grid()

    unexplored = []

    def explore(point, distance):
        if distances.get(point, distance + 1) <= distance:
            # print(f"already visited {point}")
            return
        distances[point] = distance
        unexplored.append((point, distance))

    explore(start, 0)

    while unexplored:
        (point, distance) = unexplored.pop()
        p = grid[point]
        if connects_north(p):
            n = point + N
            if connects_south(grid.get(n)):
                explore(n, distance + 1)
        if connects_south(p):
            s = point + S
            if connects_north(grid.get(s)):
                explore(s, distance + 1)
        if connects_west(p):
            w = point + W
            if connects_east(grid.get(w)):
                explore(w, distance + 1)
        if connects_east(p):
            e = point + E
            if connects_west(grid.get(e)):
                explore(e, distance + 1)

    # print_grid_distances()

    print(f"Part1: {max(distances.values())}")


if __name__ == "__main__":
    doctest.testmod()
    main()
