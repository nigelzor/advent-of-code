import doctest


def adjacent(point):
    x, y, z = point
    return [
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    ]

def main():
    lava = set()

    with open('day18_input.txt') as f:
        for line in f:
            x, y, z = [int(i) for i in line.split(',')]
            lava.add((x, y, z))

    part1 = 0
    for p in lava:
        for a in adjacent(p):
            if a not in lava:
                part1 += 1
    print(part1)

    min_x, max_x = (min(x for x, y, z in lava) - 1, max(x for x, y, z in lava) + 1)
    min_y, max_y = (min(y for x, y, z in lava) - 1, max(y for x, y, z in lava) + 1)
    min_z, max_z = (min(z for x, y, z in lava) - 1, max(z for x, y, z in lava) + 1)

    def in_bounds(point):
        x, y, z = point
        return min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z

    air = set()
    queue = [(min_x, min_y, min_z)]

    while queue:
        p = queue.pop()
        for a in adjacent(p):
            if in_bounds(a) and a not in air and a not in lava:
                air.add(a)
                queue.append(a)

    part2 = 0
    for p in lava:
        for a in adjacent(p):
            if a in air:
                part2 += 1
    print(part2)


if __name__ == "__main__":
    doctest.testmod()
    main()
