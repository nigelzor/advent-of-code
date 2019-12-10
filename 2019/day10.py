import cmath
import doctest
import math
from collections import defaultdict


def main():
    space = dict()
    with open('day10_input.txt') as f:
        for y, line in enumerate(f):
            for x, v in enumerate(line.strip()):
                if v == '#':
                    space[(x, y)] = v

    def angle(point, other):
        dx = other[0] - point[0]
        dy = other[1] - point[1]
        angle = dx + -1j * dy
        return angle

    options = []
    for point in space:
        angles = set()
        for other in space:
            if other != point:
                a = angle(point, other)
                k = "{:g}".format(a / abs(a))
                angles.add(k)
        options.append((len(angles), point))

    best = max(options)
    print(best)

    point = best[1]
    by_angle = defaultdict(list)
    for other in space:
        if other != point:
            a = angle(point, other)
            k = "{:g}".format(a / abs(a))
            by_angle[k].append(other)

    # clockwise from vertical
    def clockwise(a):
        p = -cmath.phase(a)
        if p < -(math.pi / 2):
            p += 2 * math.pi
        return p

    angles = [angle(point, x[0]) for x in by_angle.values()]
    angles = sorted(angles, key=clockwise)

    # closest first
    def distance_from_point(o):
        return abs(point[0] - o[0]) + abs(point[1] - o[1])

    for k, v in by_angle.items():
        by_angle[k] = sorted(v, key=distance_from_point, reverse=True)

    boom = 0
    while sum(len(v) for v in by_angle.values()) > 0:
        for a in angles:
            k = "{:g}".format(a / abs(a))
            if by_angle[k]:
                boom += 1
                p = by_angle[k].pop()
                # print('boom', boom, p, k, clockwise(a))
                if boom == 200:
                    print(p[0] * 100 + p[1])
                    return


if __name__ == "__main__":
    doctest.testmod()
    main()
