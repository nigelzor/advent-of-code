import doctest
import itertools
import numpy as np


def main():
    def comma_separated_ints(s):
        return [int(c.strip()) for c in s.split(',')]

    hailstones = list()
    with open('day24_input.txt') as f:
        for i, line in enumerate(f):
            position, velocity = [comma_separated_ints(s) for s in line.split('@')]
            hailstones.append((position, velocity))

    def one_hailstone_2d(h):
        (a, c, e), (b, d, f) = h
        # x = a + b * t; y = c + d * t
        # dx - by = da - bc
        return [d, -b, d * a - b * c]

    def intersect_2d(ha, hb, range):
        # print(ha, hb)
        ha_2d = one_hailstone_2d(ha)
        hb_2d = one_hailstone_2d(hb)
        try:
            m = np.linalg.solve([
                ha_2d[:2],
                hb_2d[:2]
            ], [ha_2d[-1], hb_2d[-1]])
        except np.linalg.LinAlgError:
            # presumably singular matrix
            return False

        if range[0] <= m[0] <= range[1] and range[0] <= m[1] <= range[1]:
            # print(f"inside ({m})")
            t = (m[0] - ha[0][0]) / ha[1][0]
            if t < 0:
                return False
            t = (m[0] - hb[0][0]) / hb[1][0]
            if t < 0:
                return False
            return True
        else:
            return False

    part1 = 0
    for ha, hb in itertools.combinations(hailstones, 2):
        if intersect_2d(ha, hb, (200000000000000, 400000000000000)):
            part1 += 1

    print(f'Part 1: {part1}')


if __name__ == "__main__":
    doctest.testmod()
    main()
