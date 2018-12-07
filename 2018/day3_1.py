import re
from collections import defaultdict

p = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

with open('day3.txt') as f:
    claims = defaultdict(int)
    for line in f:
        id, x, y, w, h = [int(v) for v in p.match(line).groups()]
        for xi in range(x, x+w):
            for yi in range(y, y+h):
                coord = (xi, yi)
                claims[coord] += 1
    double = 0
    for c in claims.values():
        if c > 1:
            double += 1
    print(double)
