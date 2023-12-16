import doctest
from collections import defaultdict
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

    with open('day16_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                if c != '.':
                    grid[Point(x, y)] = c

    # print_grid(grid)

    max_x = max(c.x for c in grid.keys())
    max_y = max(c.y for c in grid.keys())

    visited = defaultdict(set)
    pending = []

    def visit_next(point, direction):
        if point.x < 0 or point.x > max_x:
            return
        if point.y < 0 or point.y > max_y:
            return
        if direction not in visited[point]:
            visited[point].add(direction)
            pending.append((point, direction))

    visit_next(Point(0, 0), E)

    while pending:
        entering, direction = pending.pop()
        content = grid.get(entering)
        if content == '/':
            if direction == N:
                direction = E
            elif direction == E:
                direction = N
            elif direction == S:
                direction = W
            elif direction == W:
                direction = S
        elif content == '\\':
            if direction == N:
                direction = W
            elif direction == E:
                direction = S
            elif direction == S:
                direction = E
            elif direction == W:
                direction = N
        elif content == '-':
            if direction == N or direction == S:
                visit_next(entering + W, W)
                visit_next(entering + E, E)
                continue
        elif content == '|':
            if direction == E or direction == W:
                visit_next(entering + N, N)
                visit_next(entering + S, S)
                continue
        visit_next(entering + direction, direction)

    print(f"Part 1: {len(visited)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
