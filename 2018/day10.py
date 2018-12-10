import re
from collections import defaultdict

p = re.compile(r'.*< *(-?\d+), *(-?\d+)>.*< *(-?\d+), *(-?\d+)>')


def size(points):
    min_x = min(points.keys(), key=lambda x: x[0])[0]
    min_y = min(points.keys(), key=lambda x: x[1])[1]
    max_x = max(points.keys(), key=lambda x: x[0])[0]
    max_y = max(points.keys(), key=lambda x: x[1])[1]

    width = max_x - min_x
    height = max_y - min_y
    return (width, height)


def print_points(points):
    min_x = min(points.keys(), key=lambda x: x[0])[0]
    min_y = min(points.keys(), key=lambda x: x[1])[1]
    max_x = max(points.keys(), key=lambda x: x[0])[0]
    max_y = max(points.keys(), key=lambda x: x[1])[1]

    def fmt(x, y):
        if (x, y) in points:
            return '#'
        return ' '

    for y in range(min_y, max_y + 1):
        print(''.join(fmt(x, y) for x in range(min_x, max_x + 1)))


with open('day10.txt') as f:
    points = defaultdict(set)
    for line in f:
        px, py, vx, vy = [int(v) for v in p.match(line).groups()]
        points[(px, py)].add((vx, vy))

    s = size(points)
    a = s[0] * s[1]
    print('t={} s={} a={}'.format(0, s, a))

    for t in range(1, 20000):
        new_points = defaultdict(set)
        for (px, py), vs in points.items():
            for (vx, vy) in vs:
                # print('moving', (px, py), 'by', (vx, vy))
                new_points[(px + vx, py + vy)].add((vx, vy))
        points = new_points

        s = size(points)
        a = s[0] * s[1]
        if a < 2500:
            print('t={} s={} a={}'.format(t, s, a))
            print_points(points)

