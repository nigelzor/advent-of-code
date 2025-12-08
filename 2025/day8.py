import doctest
from itertools import combinations
from heapq import nlargest


def distance(a, b):
    # sqrt isn't necessary; sorting by distance^2 is fine
    return sum((a[i] - b[i]) ** 2 for i in range(3))


def product(xs):
    r = 1
    for x in xs:
        r *= x
    return r


def main():
    points = []

    with open("day8_input.txt") as f:
        for line in f:
            points.append(tuple(int(x) for x in line.split(",")))

    part1 = 0
    part2 = 0

    closest = sorted((distance(a, b), a, b) for a, b in combinations(points, 2))

    i = 0
    groups = []
    for _, a, b in closest:
        merge = None
        for g in groups:
            if a in g or b in g:
                if merge is None:
                    merge = g
                    merge.add(a)
                    merge.add(b)
                else:
                    merge |= g
                    g.clear()
        if not merge:
            groups.append({a, b})
        groups = [g for g in groups if g]

        i += 1
        if i == 1000:
            part1 = product(nlargest(3, (len(g) for g in groups)))
        elif len(groups) == 1 and len(groups[0]) == len(points):
            part2 = a[0] * b[0]
            break

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
