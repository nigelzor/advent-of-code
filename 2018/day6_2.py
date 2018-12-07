with open('day6.txt') as f:
    points = dict()
    max_x, max_y = (0, 0)
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
        total_distance = sum(distance(k, p) for p in points.keys())
        if total_distance < 10000:
            return True

    def xx(x):
        if x:
            return 'X'
        return '.'

    for x in range(max_x + 1):
        for y in range(max_y + 1):
            closest[x][y] = find_closest(x, y)
    for row in closest:
        print(''.join(xx(x) for x in row))
    # there's only one region

    count = 0
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            if closest[x][y]:
                count += 1
    print(count)
