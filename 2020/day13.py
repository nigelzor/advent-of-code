import doctest
import math
from itertools import count, islice


def part1(lines):
    earliest = int(lines[0])
    buses = [int(b) for b in lines[1].split(',') if b != 'x']

    arrivals = [(b, b * math.ceil(earliest / b)) for b in buses]
    best = min(arrivals, key=lambda x: x[1])
    wait = best[1] - earliest
    print(best[0] * wait)


def next_arrival(b, o, n):
    """
    >>> next_arrival(20, 0, 0)
    0
    >>> next_arrival(20, 0, 1)
    20
    >>> next_arrival(20, 2, 0)
    18
    >>> next_arrival(20, 2, 18)
    18
    >>> next_arrival(20, 2, 19)
    38
    """
    return b * math.ceil((n + o) / b) - o


def wheel(b, o):
    """
    >>> list(islice(wheel(10, 0), 3))
    [10, 20, 30]
    >>> list(islice(wheel(7, 2), 3))
    [5, 12, 19]
    """
    return count(b - o, b)


def combine_wheels_slow(a, b):
    """
    >>> list(islice(combine_wheels_slow(wheel(7, 2), wheel(3, 0)), 3))
    [12, 33, 54]
    """
    la = next(a)
    lb = next(b)
    while True:
        if la == lb:
            yield la
        if la < lb:
            la = next(a)
        else:
            lb = next(b)


def combine_wheels_fast(a, b):
    """
    >>> list(islice(combine_wheels_fast(wheel(7, 2), wheel(3, 0)), 3))
    [12, 33, 54]
    """
    slow = list(islice(combine_wheels_slow(a, b), 4))
    start = slow[0]
    delta1 = slow[1] - slow[0]
    delta2 = slow[2] - slow[1]
    delta3 = slow[3] - slow[2]
    assert delta1 == delta2
    assert delta1 == delta3
    return count(start, delta1)


def part2(line1):
    """
    >>> part2('17,x,13,19')
    3417
    >>> part2('67,7,59,61')
    754018
    >>> part2('67,x,7,59,61')
    779210
    >>> part2('67,7,x,59,61')
    1261476
    >>> part2('1789,37,47,1889')
    1202161486
    """
    buses = [(int(b), offset) for offset, b in enumerate(line1.split(',')) if b != 'x']
    buses.sort(key=lambda b: -b[0])

    wheels = [wheel(b, o) for b, o in buses]
    final = None
    for w in wheels:
        if final is None:
            final = w
        else:
            final = combine_wheels_fast(final, w)
    return next(final)


def main():
    with open('day13_input.txt') as file:
        lines = file.readlines()

    # part1(lines)
    # part2(lines[1])


if __name__ == "__main__":
    doctest.testmod()
    main()
