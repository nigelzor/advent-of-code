import doctest
import re
from heapq import heappush, heappop

p = re.compile(r'pos=< *(-?\d+), *(-?\d+), *(-?\d+)>.*r=(-?\d+)')


def manhattan(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))


def distance_to_range(x, range):
    """
    >>> distance_to_range(0, (2, 2))
    2
    >>> distance_to_range(0, (0, 2))
    0
    >>> distance_to_range(2, (0, 2))
    0
    >>> distance_to_range(4, (2, 2))
    2
    """
    if x < range[0]:
        return range[0] - x
    if x <= range[1]:
        return 0
    return x - range[1]


def reaches_region(p, r, region):
    """
    >>> reaches_region((10, 12, 12), 2, ((12, 12), (12, 12), (12, 12)))
    True
    >>> reaches_region((10, 10, 10), 5, ((12, 12), (12, 12), (12, 12)))
    False
    >>> reaches_region((10, 10, 10), 5, ((12, 12), (12, 12), (12, 12)))
    False
    """
    for i in range(3):
        r -= distance_to_range(p[i], region[i])
    return r >= 0


def max_edge_length(region):
    return max(a[1] - a[0] for a in region)


def corners(region):
    for x in region[0]:
        for y in region[1]:
            for z in region[2]:
                yield x, y, z


def subdivide(range):
    """
    >>> subdivide((-1, 4))
    [(-1, 1), (2, 4)]
    >>> subdivide((-1, 3))
    [(-1, 1), (2, 3)]
    >>> subdivide((0, 1))
    [(0, 0), (1, 1)]
    >>> subdivide((1, 1))
    [(1, 1)]
    """
    d0, d1 = range
    length = d1 - d0
    if length == 0:
        return [range]
    midpoint = d0 + (length // 2)
    return [(d0, midpoint), (midpoint + 1, d1)]


def main():
    with open('day23.txt') as f:
        points = dict()
        for line in f:
            nx, ny, nz, r = [int(v) for v in p.match(line).groups()]
            points[(nx, ny, nz)] = r

        strongest = max(points.items(), key=lambda x: x[1])
        print('strongest', strongest)

        in_range = sum(1 for point in points.keys() if manhattan(point, strongest[0]) <= strongest[1])
        print('in_range', in_range)

        bounds = [(min(k[i] for k in points), max(k[i] for k in points)) for i in range(3)]

        def score_region(region):
            n = sum(1 for p, r in points.items() if reaches_region(p, r, region))
            # maximize n, minimize volume, minimize distance
            distances_to_zero = [manhattan((0, 0, 0), v) for v in corners(region)]
            return -n, max_edge_length(region), max(distances_to_zero)

        queue = []
        heappush(queue, (score_region(bounds), bounds))

        while queue:
            score, region = heappop(queue)
            if max_edge_length(region) == 0:
                print('best', score, tuple(r[0] for r in region))
                break
            xs = subdivide(region[0])
            ys = subdivide(region[1])
            zs = subdivide(region[2])
            for x in xs:
                for y in ys:
                    for z in zs:
                        child_region = (x, y, z)
                        heappush(queue, (score_region(child_region), child_region))


if __name__ == '__main__':
    doctest.testmod()
    main()
