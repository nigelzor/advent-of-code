import cmath
import doctest
import math
from collections import defaultdict


def clockwise_angle(point, other, y_scale=1):
    """
    >>> clockwise_angle((0, 0), (0, 1))
    0.0
    >>> clockwise_angle((0, 0), (1, 1))
    45.0
    >>> clockwise_angle((0, 0), (1, 0))
    90.0
    >>> clockwise_angle((0, 0), (1, -1))
    135.0
    >>> clockwise_angle((0, 0), (0, -1))
    180.0
    >>> clockwise_angle((0, 0), (-1, -1))
    225.0
    >>> clockwise_angle((0, 0), (-1, 0))
    270.0
    >>> clockwise_angle((0, 0), (-1, 1))
    315.0
    """
    dx = other[0] - point[0]
    dy = (other[1] - point[1]) * y_scale
    phase = -cmath.phase(dx + dy * 1j)
    angle = 90 + math.degrees(phase)
    if angle < 0:
        angle += 360
    return angle


def main():
    space = []
    with open('day10_input.txt') as f:
    # with open('day10_sample4.txt') as f:
        for y, line in enumerate(f):
            for x, v in enumerate(line.strip()):
                if v == '#':
                    space.append((x, y))

    options = []
    for point in space:
        angles = set()
        for other in space:
            if other != point:
                angles.add(clockwise_angle(point, other))
        options.append((len(angles), point))

    best = max(options)
    print(best)

    point = best[1]
    by_angle = defaultdict(list)
    for other in space:
        if other != point:
            a = clockwise_angle(point, other, y_scale=-1)
            by_angle[a].append(other)

    angles = sorted(by_angle.keys())

    # closest first
    def distance_from_point(o):
        return abs(point[0] - o[0]) + abs(point[1] - o[1])

    for k, v in by_angle.items():
        by_angle[k] = sorted(v, key=distance_from_point, reverse=True)

    boom = 0
    while sum(len(v) for v in by_angle.values()) > 0:
        for a in angles:
            if by_angle[a]:
                boom += 1
                p = by_angle[a].pop()
                # print('boom', boom, p, a)
                if boom == 200:
                    print(p[0] * 100 + p[1])
                    return


if __name__ == "__main__":
    doctest.testmod()
    main()
