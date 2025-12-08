import doctest


def invalid_1(x):
    """
    >>> invalid_1(55)
    True
    >>> invalid_1(123123)
    True
    >>> invalid_1(101)
    False
    """
    s = str(x)
    l = len(s)
    if l % 2 == 1:
        return False
    hl = l // 2
    for i in range(hl):
        if s[i] != s[i + hl]:
            return False
    return True


def invalid_2(x):
    """
    >>> invalid_2(12341234)
    True
    >>> invalid_2(123123123)
    True
    >>> invalid_2(1212121212)
    True
    >>> invalid_2(1111111)
    True
    """
    s = str(x)
    l = len(s)
    if l < 2:
        return False
    # length 1
    if all(c == s[0] for c in s[1:]):
        return True
    # length 2
    if l % 2 == 0:
        gl = l // 2
        for i in range(gl):
            if s[i] != s[i + gl]:
                break
        else:
            return True
    # length 3
    if l % 3 == 0:
        gl = l // 3
        for i in range(gl):
            if s[i] != s[i + gl] or s[i] != s[i + 2 * gl]:
                break
        else:
            return True
    # length 4
    if l % 4 == 0:
        gl = l // 4
        for i in range(gl):
            if s[i] != s[i + gl] or s[i] != s[i + 2 * gl] or s[i] != s[i + 3 * gl]:
                break
        else:
            return True
    # length 5
    if l % 5 == 0:
        gl = l // 5
        for i in range(gl):
            if (
                s[i] != s[i + gl]
                or s[i] != s[i + 2 * gl]
                or s[i] != s[i + 3 * gl]
                or s[i] != s[i + 4 * gl]
            ):
                break
        else:
            return True
    return False


def main():
    with open("day2_input.txt") as f:
        for line in f:
            ranges = [tuple(map(int, r.split("-"))) for r in line.split(",")]

    part1 = 0
    part2 = 0
    for start, end in ranges:
        for x in range(start, end + 1):
            if invalid_1(x):
                part1 += x
            if invalid_2(x):
                part2 += x

    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
