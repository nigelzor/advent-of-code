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
    grid = dict()
    distances = dict()
    start = None

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

    def make_doubled_grid():
        doubled = dict()
        for p in distances.keys():
            a = grid[p]
            doubled[p * 2] = a

            b = grid.get(p + S)
            if connects_south(a) and connects_north(b):
                doubled[p * 2 + S] = '|'

            b = grid.get(p + E)
            if connects_east(a) and connects_west(b):
                doubled[p * 2 + E] = '-'

        return doubled

    with open('day10_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                if c != ".":
                    grid[Point(x, y)] = c
                if c == "S":
                    start = Point(x, y)

    unexplored = []

    def explore(point, distance):
        if distances.get(point, distance + 1) <= distance:
            # print(f"already visited {point}")
            return
        distances[point] = distance
        unexplored.append((point, distance))

    explore(start, 0)

    def connections(point):
        p = grid[point]
        if connects_north(p):
            n = point + N
            if connects_south(grid.get(n)):
                yield n
        if connects_south(p):
            s = point + S
            if connects_north(grid.get(s)):
                yield s
        if connects_west(p):
            w = point + W
            if connects_east(grid.get(w)):
                yield w
        if connects_east(p):
            e = point + E
            if connects_west(grid.get(e)):
                yield e

    while unexplored:
        (point, distance) = unexplored.pop()
        for c in connections(point):
            explore(c, distance + 1)
    print(f"Part1: {max(distances.values())}")

    minx, maxx, miny, maxy = bounds(grid)
    dg = make_doubled_grid()

    pending = [Point(0, 0)]
    while pending:
        point = pending.pop()
        if point.x < minx or point.x > maxx * 2 or point.y < miny or point.y > maxy * 2:
            continue
        if point not in dg:
            dg[point] = 'O'
            pending.append(point + N)
            pending.append(point + E)
            pending.append(point + S)
            pending.append(point + W)

    # print_grid(dg)
    enclosed = 0
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            if Point(x * 2, y * 2) not in dg:
                enclosed += 1
    print(f"Part 2: {enclosed}")


if __name__ == "__main__":
    doctest.testmod()
    main()
