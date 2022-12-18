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
    map = dict()

    with open('day18_input.txt') as f:
        for line in f:
            x, y, z = [int(i) for i in line.split(',')]
            map[(x, y, z)] = True

    surface_area = 0
    for p in map:
        for a in adjacent(p):
            if a not in map:
                surface_area += 1
    print(surface_area)



if __name__ == "__main__":
    doctest.testmod()
    main()
