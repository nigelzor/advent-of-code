import doctest
import math


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


def part1(lines):
    earliest = int(lines[0])
    buses = [int(b) for b in lines[1].split(',') if b != 'x']

    arrivals = [(b, b * math.ceil(earliest / b)) for b in buses]
    best = min(arrivals, key=lambda x: x[1])
    wait = best[1] - earliest
    print(best[0] * wait)


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
    # limit = math.lcm(*[b for b, o in buses])

    buses.sort(key=lambda b: -b[0])
    # print(buses)
    # [(733, 23), (449, 54), (41, 13), (37, 91), (29, 52), (23, 0), (19, 42), (17, 37), (13, 36)]
    least_t = 0
    while True:
        for b, o in buses:
            t = next_arrival(b, o, least_t)
            if t > least_t:
                least_t = t
                break
        else:
            break
    return least_t


def main():
    with open('day13_input.txt') as file:
        lines = file.readlines()

    # part1(lines)
    part2(lines[1])


if __name__ == "__main__":
    doctest.testmod()
    main()
