import doctest


def adjacent_or_overlapping(a, b):
    if a[1] + 1 >= b[0]:
        return True
    return False


def combine_ranges(ranges):
    """
    >>> combine_ranges([(0, 2), (1, 3)])
    [(0, 3)]
    """
    ranges = sorted(ranges)
    for i in range(1, len(ranges)):
        a = ranges[i - 1]
        b = ranges[i]
        if adjacent_or_overlapping(a, b):
            ranges[i - 1] = None
            ranges[i] = (min(a[0], b[0]), max(a[1], b[1]))
    return [r for r in ranges if r]


def main():
    ranges = []
    available = []

    with open("day5_input.txt") as f:
        for line in f:
            line = line.strip()

            if "-" in line:
                lo, hi = [int(x) for x in line.split("-")]

                ranges.append((lo, hi))

            elif line:
                available.append(int(line))

    part1 = 0
    part2 = 0

    ranges = combine_ranges(ranges)

    for i in available:
        if any(r[0] <= i <= r[1] for r in ranges):
            part1 += 1

    part2 = sum(r[1] - r[0] + 1 for r in ranges)

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
