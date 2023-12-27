import doctest
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
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


def bounds(g):
    min_x = min(c.x for c in g.keys())
    max_x = max(c.x for c in g.keys())
    min_y = min(c.y for c in g.keys())
    max_y = max(c.y for c in g.keys())
    return min_x, max_x, min_y, max_y


def print_grid(g):
    minx, maxx, miny, maxy = bounds(g)
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            print(g.get(Point(x, y), '.'), end='')
        print('')


def main():
    start = None
    end = None
    grid = dict()

    with open('day23_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                p = Point(x, y)
                if c == '.':
                    if start is None:
                        start = p
                    end = p
                grid[p] = c

    pending_paths = [(start,)]
    found_paths = []

    while pending_paths:
        path = pending_paths.pop()

        for direction in [N, E, S, W]:
            next_step = path[-1] + direction
            if next_step == end:
                found_paths.append(path + (next_step,))
            else:
                ground = grid.get(next_step, '#')
                if ground == '#' or next_step in path:
                    continue
                if ground == '.' or (ground == '^' and direction == N) or (ground == '>' and direction == E) \
                        or (ground == 'v' and direction == S) or (ground == '<' and direction == W):
                    pending_paths.append(path + (next_step,))

    print(f"Part 1: {max(len(p) - 1 for p in found_paths)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
