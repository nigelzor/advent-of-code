import doctest

DIRECTIONS = {
    'U': 1j,
    'R': 1,
    'L': -1,
    'D': -1j,
}


def main():
    lines = []

    with open('day3_input.txt') as f:
        for line in f:
            lines.append((x[0], int(x[1:])) for x in line.split(','))

    def travel(line):
        grid = dict()
        p = 0
        d = 0
        for direction, distance in line:
            for _ in range(distance):
                d += 1
                p += DIRECTIONS[direction]
                if p not in grid:
                    grid[p] = d
        return grid

    a = travel(lines[0])
    b = travel(lines[1])

    intersections = a.keys() & b.keys()
    print(min(abs(p.real) + abs(p.imag) for p in intersections))
    print(min(a[p] + b[p] for p in intersections))


if __name__ == "__main__":
    doctest.testmod()
    main()
