import doctest


def count_zeroes(position, distance):
    """
    >>> count_zeroes(0, 1)
    0
    >>> count_zeroes(0, 100)
    1
    >>> count_zeroes(1, 100)
    1
    >>> count_zeroes(99, 1)
    1
    >>> count_zeroes(99, 2)
    1
    >>> count_zeroes(99, 101)
    2
    >>> count_zeroes(1, -1)
    1
    >>> count_zeroes(1, -102)
    2
    """
    zeroes = 0
    while distance != 0:
        if distance > 0:
            take = min(100 - position, distance)
        else:
            take = -min(position or 100, -distance)
        distance -= take
        position = (position + take) % 100
        if position == 0:
            zeroes += 1
    return zeroes


def main():
    password = []
    with open("day1_input.txt") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:])
            if direction == "R":
                password.append(distance)
            else:
                password.append(-distance)

    position = 50
    part1 = 0
    part2 = 0

    for a in password:
        part2 += count_zeroes(position, a)
        position = (position + a) % 100
        if position == 0:
            part1 += 1

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
