from collections import Counter

sample = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

with open('day6.txt') as f:
    points = dict()
    max_x, max_y = (0, 0)
    # for line in sample.split("\n"):
    for line in f:
        x, y = [int(v) for v in line.split(', ')]
        points[(x, y)] = True
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    print(max_x)
    print(max_y)
    closest = [[None for y in range(max_y + 1)] for x in range(max_x + 1)]

    def distance(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_closest(x, y):
        k = (x, y)
        if k in points:
            return k
        distances = [(p, distance(k, p)) for p in points.keys()]
        distances.sort(key=lambda k: k[1])
        min = distances[0][1]
        closest = [d[0] for d in distances if d[1] == min]
        if len(closest) > 1:
            return None
        return closest[0]

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            closest[x][y] = find_closest(x, y)
    # for row in closest:
    #     print(row)

    common = Counter()
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if closest[x][y]:
                common[closest[x][y]] += 1

    infinite = Counter()
    for x in range(0, max_x + 1):
        for y in (0, max_y):
            infinite[closest[x][y]] += 1
    for x in (0, max_x):
        for y in range(1, max_y):
            infinite[closest[x][y]] += 1

    # print(infinite)
    for c in infinite.keys():
        del common[c]

    print(common.most_common(3))
