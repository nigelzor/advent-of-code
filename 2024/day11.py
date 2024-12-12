import doctest
from functools import lru_cache


def blink(stone):
    """
    >>> blink(0)
    (1,)
    >>> blink(1)
    (2024,)
    >>> blink(2024)
    (20, 24)
    """
    if stone == 0:
        return (1,)
    ss = str(stone)
    sl = len(ss)
    if sl % 2 == 0:
        mid = sl // 2
        return int(ss[:mid]), int(ss[mid:])
    return (stone * 2024,)


def length_after(stone, n):
    if n == 0:
        return 1
    return length_after_(stone, n)


@lru_cache(2048)
def length_after_(stone, n):
    return sum(length_after(s, n - 1) for s in blink(stone))


def part1(stones):
    return sum(length_after(s, 25) for s in stones)


def part2(stones):
    return sum(length_after(s, 75) for s in stones)


def main():
    with open("day11_input.txt") as f:
        stones = [int(s) for s in f.readline().split()]

    print(f"part 1: {part1(stones)}")
    print(f"part 2: {part2(stones)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
