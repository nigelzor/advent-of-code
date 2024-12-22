import doctest
from itertools import islice, pairwise


def pseudorandom(secret):
    """
    >>> list(islice(pseudorandom(123), 10))
    [15887950, 16495136, 527345, 704524, 1553684, 12683156, 11100544, 12249484, 7753432, 5908254]
    """
    while True:
        secret ^= secret * 64
        secret %= 16777216
        secret ^= secret // 32
        secret %= 16777216
        secret ^= secret * 2048
        secret %= 16777216
        yield secret


def part1(secret):
    """
    >>> part1(1)
    8685429
    """
    return next(islice(pseudorandom(secret), 1999, 2000))


def price_seq(secret):
    """
    >>> list(islice(price_seq(123), 10))
    [3, 0, 6, 5, 4, 4, 6, 4, 4, 2]
    """
    yield secret % 10
    yield from islice((n % 10 for n in pseudorandom(secret)), 2000)


def change_seq(g):
    """
    >>> list(islice(change_seq(price_seq(123)), 9))
    [-3, 6, -1, -1, 0, 2, -2, 0, -2]
    >>> sum(1 for _ in change_seq(price_seq(123)))
    2000
    """
    return (current - previous for previous, current in pairwise(g))


def window(seq, n):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def price_info(secret):
    """
    >>> list(islice(price_info(123), 3))
    [(4, (-3, 6, -1, -1)), (4, (6, -1, -1, 0)), (6, (-1, -1, 0, 2))]
    """
    price = islice(price_seq(secret), 4, None)
    change = window(change_seq(price_seq(secret)), 4)
    return zip(price, change)


def build_price_map(secret):
    pm = dict()
    for price, changes in price_info(secret):
        if changes not in pm:
            pm[changes] = price
    return pm


def part2(buyers):
    price_maps = [build_price_map(b) for b in buyers]
    changes = {c for pm in price_maps for c in pm}

    return max(sum(pm.get(change, 0) for pm in price_maps) for change in changes)


def main():
    with open("day22_input.txt") as f:
        buyers = [int(line.strip()) for line in f]

    print(f"part 1: {sum(part1(b) for b in buyers)}")
    print(f"part 2: {part2(buyers)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
