import doctest
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
    best_by_direction = dict()

    def add(point, total_loss, history):
        if point not in best or best[point][0] > total_loss:
            best[point] = (total_loss, history)
            if point == destination:
                print(f"new best: {total_loss}")

        if history:
            last = history[-1]
            if (point, last) not in best_by_direction or best_by_direction[(point, last)] > total_loss:
                best_by_direction[(point, last)] = total_loss
            else:
                return

        # score = target to minimise
        score = (manhattan(point, destination) + 1) * total_loss
        heappush(pending, (score, total_loss, point, history))

    add(Point(0, 0), 0, ())

    def available_directions_part1(history):
        for direction in (N, E, S, W):
            if history:
                last, n = tail_summary(history)
                if last == direction * -1:
                    continue
                if last == direction and n >= 3:
                    continue
            yield direction

    def part2_next_step_options(history):
        options = [N, E, S, W]
        if history:
            last = history[-1]
            options.remove(last)
            options.remove(last * -1)

        for direction in options:
            for distance in range(4, 10 + 1):
                yield direction, distance

    while pending:
        _score, total_loss, point, history = heappop(pending)

        for direction, distance in part2_next_step_options(history):
            next_point = point + direction * distance
            if next_point.x < 0 or next_point.x > max_x:
                continue
            if next_point.y < 0 or next_point.y > max_y:
                continue
            next_point = point
            next_total_loss = total_loss
            for _ in range(distance):
                next_point += direction
                next_total_loss += grid[next_point]
            add(next_point, next_total_loss, history + (direction,) * distance)

    print()
    print_grid_path(grid, best[destination][1])
    print()
    print(f"Part 2: {best[destination][0]}")


if __name__ == "__main__":
    doctest.testmod()
    main()
