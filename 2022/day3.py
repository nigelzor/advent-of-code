import doctest


def priority(c):
    """
    >>> priority('a')
    1
    >>> priority('A')
    27
    """
    p = ord(c)
    if p >= ord('a'):
        return p - ord('a') + 1
    return p - ord('A') + 27


def main():
    group = []
    part1 = 0
    part2 = 0
    with open('day3_input.txt') as f:
        for line in f:
            line = line.strip()
            mid = len(line) // 2
            a, b = line[:mid], line[mid:]
            common = set(a) & set(b)
            part1 += priority(next(iter(common)))

            group.append(line)
            if len(group) == 3:
                common = set(group[0]) & set(group[1]) & set(group[2])
                part2 += priority(next(iter(common)))
                group = []

    print(part1)
    print(part2)


if __name__ == "__main__":
    doctest.testmod()
    main()
