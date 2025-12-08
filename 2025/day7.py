import doctest
from collections import defaultdict


def product(xs):
    r = 1
    for x in xs:
        r *= x
    return r


def main():
    diagram = {}

    with open("day7_input.txt") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                if c == "^":
                    diagram[(x, y)] = c
                if c == "S":
                    start = (x, y)
    max_y = y

    part1 = 0
    part2 = 0

    beams = {start[0]: 1}
    for y in range(start[1], max_y + 1):
        new_beams = defaultdict(int)
        for x, c in beams.items():
            if diagram.get((x, y)) == "^":
                part1 += 1
                new_beams[x - 1] += c
                new_beams[x + 1] += c
            else:
                new_beams[x] += c
        beams = new_beams

    part2 = sum(beams.values())

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
