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

    direction_map = {
        'U': N,
        'D': S,
        'L': W,
        'R': E,
    }

    lines_1 = []
    lines_2 = []
    with open('day18_input.txt') as f:
        for line in f:
            direction, distance, color = line_pattern.match(line).groups()
            direction = direction_map[direction]
            distance = int(distance)
            lines_1.append((direction, distance))

            distance = int(color[:-1], 16)
            direction = (E, S, W, N)[int(color[-1])]
            lines_2.append((direction, distance))

    def extend_possibilities(items):
        options = set()
        for item in items:
            options.add(item)
            options.add(item + 1)
            options.add(item - 1)
        return sorted(options)

    def contained_area(lines):
        ys = [0]
        xs = [0]
        for direction, distance in lines:
            if direction == N:
                ys.append(ys[-1] - distance)
            elif direction == S:
                ys.append(ys[-1] + distance)
            elif direction == E:
                xs.append(xs[-1] + distance)
            elif direction == W:
                xs.append(xs[-1] - distance)
        xs = extend_possibilities(xs)
        ys = extend_possibilities(ys)

        grid = dict()
        position = Point(0, 0)
        for direction, distance in lines:
            if direction == E:
                y_idx = ys.index(position.y)
                for x_idx, x in enumerate(xs):
                    if position.x < x <= position.x + distance:
                        grid[Point(x_idx, y_idx)] = '#'
            if direction == W:
                y_idx = ys.index(position.y)
                for x_idx, x in enumerate(xs):
                    if position.x - distance <= x < position.x:
                        grid[Point(x_idx, y_idx)] = '#'
            if direction == S:
                x_idx = xs.index(position.x)
                for y_idx, y in enumerate(ys):
                    if position.y < y < position.y + distance + 1:
                        grid[Point(x_idx, y_idx)] = '#'
            if direction == N:
                x_idx = xs.index(position.x)
                for y_idx, y in enumerate(ys):
                    if position.y - distance <= y < position.y:
                        grid[Point(x_idx, y_idx)] = '#'

            position += direction * distance

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

        total_area = 0
        last_y = -1
        for y_idx, y in enumerate(ys):
            last_x = -1
            for x_idx, x in enumerate(xs):
                if grid.get(Point(x_idx, y_idx), '.') in ".#":
                    total_area += (y - last_y) * (x - last_x)
                last_x = x
            last_y = y
        return total_area

    print(f'Part 1: {contained_area(lines_1)}')
    print(f'Part 2: {contained_area(lines_2)}')


if __name__ == "__main__":
    doctest.testmod()
    main()
