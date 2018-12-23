import re

p = re.compile(r'pos=< *(-?\d+), *(-?\d+), *(-?\d+)>.*r=(-?\d+)')


def manhattan(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))


with open('day23.txt') as f:
    points = dict()
    for line in f:
        nx, ny, nz, r = [int(v) for v in p.match(line).groups()]
        points[(nx, ny, nz)] = r

    strongest = max(points.items(), key=lambda x: x[1])
    print('strongest', strongest)

    in_range = sum(1 for point in points.keys() if manhattan(point, strongest[0]) <= strongest[1])
    print('in_range', in_range)
