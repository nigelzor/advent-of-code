import doctest
from collections import defaultdict
from dataclasses import dataclass
from heapq import heappop, heappush


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


def dir_to_arrow(d):
    return {
        N: "^",
        S: "v",
        E: ">",
        W: "<",
    }[d]


def arrows(ds):
    return ''.join(dir_to_arrow(d) for d in ds)


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


def print_grid_path(g, path):
    g = g.copy()
    p = Point(0, 0)
    for step in path:
        p += step
        g[p] = dir_to_arrow(step)

    minx, maxx, miny, maxy = bounds(g)
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            print(g.get(Point(x, y), '.'), end='')
        print('')


def tail_summary(seq):
    """
    >>> tail_summary("hello")
    ('o', 1)
    >>> tail_summary(">>>vv")
    ('v', 2)
    >>> tail_summary("x")
    ('x', 1)
    """
    seq = iter(reversed(seq))
    last = next(seq)
    count = 1
    for c in seq:
        if c != last:
            break
        count += 1
    return last, count


def main():
    grid = dict()

    with open('day17_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                grid[Point(x, y)] = int(c)

    # print_grid(grid)

    max_x = max(c.x for c in grid.keys())
    max_y = max(c.y for c in grid.keys())
    destination = Point(max_x, max_y)

    pending = []
    best = dict()
    best_by_direction = defaultdict(lambda: defaultdict(dict))

    def add(point, total_loss, history):
        if point not in best or best[point][0] > total_loss:
            best[point] = (total_loss, history)
            if point == destination:
                print(f"new best: {total_loss}")

        if history:
            last, n = tail_summary(history)
            bbd = best_by_direction[point][last]
            any_better = False
            for n_or_more in range(n, 4):
                if n_or_more not in bbd or bbd[n_or_more] > total_loss:
                    bbd[n_or_more] = total_loss
                    any_better = True
            if not any_better:
                return

        # score = target to minimise
        score = (manhattan(point, destination) + 1) * total_loss
        heappush(pending, (score, total_loss, point, history))

    add(Point(0, 0), 0, ())

    while pending:
        _score, total_loss, point, history = heappop(pending)

        for direction in (N, E, S, W):
            next_point = point + direction
            if next_point.x < 0 or next_point.x > max_x:
                continue
            if next_point.y < 0 or next_point.y > max_y:
                continue
            if history:
                last, n = tail_summary(history)
                if last == direction * -1:
                    continue
                if last == direction and n >= 3:
                    continue

            next_total_loss = total_loss + grid[next_point]
            add(next_point, next_total_loss, history + (direction,))

    print()
    print_grid_path(grid, best[destination][1])
    print()
    print(f"Part 1: {best[destination][0]}")


if __name__ == "__main__":
    doctest.testmod()
    main()
