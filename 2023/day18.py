import doctest
import re
from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Point(self.x * other, self.y * other)


def manhattan(a: Point, b: Point):
    return abs(a.x - b.x) + abs(a.y - b.y)


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)


def left(d):
    return {
        N: W,
        S: E,
        E: N,
        W: S,
    }[d]


def right(d):
    return {
        N: E,
        S: W,
        E: S,
        W: N,
    }[d]


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
    line_pattern = re.compile(r"(.) (\d+) \(#(.{6})\)")
    grid = dict()

    direction_map = {
        'U': N,
        'D': S,
        'L': W,
        'R': E,
    }

    lines = []
    with open('day18_input.txt') as f:
        for line in f:
            direction, distance, color = line_pattern.match(line).groups()
            direction = direction_map[direction]
            distance = int(distance)
            lines.append((direction, distance, color))

    position = Point(0, 0)
    for (direction, distance, color) in lines:
        for _ in range(distance):
            position += direction
            grid[position] = '#'

    # print_grid(grid)

    min_x, max_x, min_y, max_y = bounds(grid)
    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1

    pending = [Point(min_x, min_y)]
    while pending:
        position = pending.pop()
        grid[position] = ' '
        for direction in (N, S, E, W):
            next_position = position + direction
            if min_x <= next_position.x <= max_x and min_y <= next_position.y <= max_y:
                if grid.get(next_position) is None:
                    pending.append(next_position)

    # print_grid(grid)

    part1 = (max_x - min_x + 1) * (max_y - min_y + 1) - sum(1 for v in grid.values() if v == ' ')
    print(f'Part 1: {part1}')


if __name__ == "__main__":
    doctest.testmod()
    main()
