import doctest


def adjacent(x, y):
    return [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]


def count_adjacent(diagram, p):
    x, y = p
    return sum(1 for a in adjacent(x, y) if a in diagram)


def main():
    diagram = {}
    with open("day4_input.txt") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                if c == "@":
                    diagram[(x, y)] = c

    part1 = 0
    part2 = 0

    for p in diagram.keys():
        if count_adjacent(diagram, p) < 4:
            part1 += 1

    while True:
        to_remove = []
        for p in diagram.keys():
            if count_adjacent(diagram, p) < 4:
                to_remove.append(p)
        if to_remove:
            for p in to_remove:
                del diagram[p]
            part2 += len(to_remove)
        else:
            break

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
