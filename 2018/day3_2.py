import re
from collections import defaultdict

p = re.compile('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

with open('day3.txt') as f:
    ids = set()
    claims = defaultdict(set)
    for line in f:
        id, x, y, w, h = [int(v) for v in p.match(line).groups()]
        ids.add(id)
        for xi in range(x, x+w):
            for yi in range(y, y+h):
                coord = (xi, yi)
                claims[coord].add(id)
    for c in claims.values():
        if len(c) > 1:
            for id in c:
                ids.discard(id)
    print(ids)
