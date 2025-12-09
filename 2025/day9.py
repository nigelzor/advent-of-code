import doctest
from itertools import combinations


def area(a, b):
    return product(abs(a[i] - b[i]) + 1 for i in range(2))


def product(xs):
    r = 1
    for x in xs:
        r *= x
    return r


def line_between(a, b):
    if a[0] == b[0]:
        return ((a[0], y) for y in range(min(a[1], b[1]) + 1, max(a[1], b[1])))
    return ((x, a[1]) for x in range(min(a[0], b[0]) + 1, max(a[0], b[0])))


def main():
    points = []

    with open("day9_input.txt") as f:
        for line in f:
            points.append(tuple(int(x) for x in line.split(",")))

    part1, _, _ = max((area(a, b), a, b) for a, b in combinations(points, 2))
    print(f"part 1: {part1}")

    xs = sorted({p[0] for p in points})
    ys = sorted({p[1] for p in points})
    reduced_xs = {x: i for i, x in enumerate(xs)}
    reduced_ys = {y: i for i, y in enumerate(ys)}

    def reduce_point(p):
        return reduced_xs[p[0]], reduced_ys[p[1]]

    def expand_point(p):
        return xs[p[0]], ys[p[1]]

    reduced_points = [reduce_point(p) for p in points]

    grid = {}
    last = reduced_points[-1]
    for point in reduced_points:
        grid[point] = "#"
        for c in line_between(point, last):
            grid[c] = "X"
        last = point

    initial = min(grid.keys())
    initial = (initial[0] + 1, initial[1] + 1)  # assuming concavity?

    filling = [initial]
    while filling:
        p = filling.pop()
        if p not in grid:
            grid[p] = "X"
            x, y = p
            filling.append((x, y + 1))
            filling.append((x, y - 1))
            filling.append((x + 1, y))
            filling.append((x - 1, y))

    # for y in range(initial[1] - 10, initial[1] + 10):
    #    for x in range(initial[0] - 10, initial[0] + 10):
    #        print(grid.get((x, y), ' '), end='')
    #    print('')

    def contained(a, b):
        xrange = range(min(a[0], b[0]), max(a[0], b[0]) + 1)
        yrange = range(min(a[1], b[1]), max(a[1], b[1]) + 1)
        for x in xrange:
            for y in yrange:
                if (x, y) not in grid:
                    return False
        return True

    part2 = max(
        area(expand_point(a), expand_point(b))
        for a, b in combinations(reduced_points, 2)
        if contained(a, b)
    )
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
