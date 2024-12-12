import doctest


def blink_one(stone):
    """
    >>> blink_one(0)
    1
    >>> blink_one(1)
    2024
    >>> blink_one(2024)
    (20, 24)
    """
    if stone == 0:
        return 1
    ss = str(stone)
    sl = len(ss)
    if sl % 2 == 0:
        mid = sl // 2
        return int(ss[:mid]), int(ss[mid:])
    return stone * 2024


def blink_all(stones):
    """
    >>> blink_all([125, 17])
    [253000, (1, 7)]
    """
    if isinstance(stones, (list, tuple)):
        return [blink_all(s) for s in stones]
    return blink_one(stones)


def stones_length(stones):
    if isinstance(stones, (list, tuple)):
        return sum(stones_length(s) for s in stones)
    return 1


def part1(stones):
    for i in range(25):
        stones = blink_all(stones)
    return stones_length(stones)


def part2(stones):
    for i in range(75):
        stones = blink_all(stones)
        print(stones_length(stones))
    return stones_length(stones)


def main():
    with open("day11_input.txt") as f:
        stones = [int(s) for s in f.readline().split()]

    print(f"part 1: {part1(stones)}")
    print(f"part 2: {part2(stones)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
