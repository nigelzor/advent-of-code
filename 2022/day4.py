import doctest


def contains(a, b):
    return a.start <= b.start and a.stop >= b.stop


def overlaps(a, b):
    return set(a) & set(b)


def main():
    part1 = 0
    part2 = 0
    with open('day4_input.txt') as f:
        for line in f:
            line = line.strip()
            [first, second] = [range(int(a), int(b) + 1) for a, b in (r.split('-') for r in line.split(','))]
            if contains(first, second) or contains(second, first):
                part1 += 1
            if overlaps(first, second):
                part2 += 1

    print(part1)
    print(part2)


if __name__ == "__main__":
    doctest.testmod()
    main()
