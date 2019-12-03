import doctest


def allocate_ways(remaining, containers):
    """
    >>> allocate_ways(10, [10])
    1
    >>> allocate_ways(25, [20, 15, 10, 5, 5])
    4
    """
    if remaining == 0:
        return 1
    if not containers:
        return 0
    options = 0
    using = containers[0]
    if using <= remaining:
        options += allocate_ways(remaining - using, containers[1:])
    options += allocate_ways(remaining, containers[1:])
    return options


def min_allocate_ways(n, remaining, containers):
    """
    >>> min_allocate_ways(0, 10, [10])
    (1, 1)
    >>> min_allocate_ways(0, 25, [20, 15, 10, 5, 5])
    (2, 3)
    """
    if remaining == 0:
        return n, 1
    if not containers:
        return float('Inf'), 0
    using = containers[0]

    a = min_allocate_ways(n, remaining, containers[1:])
    if using <= remaining:
        b = min_allocate_ways(n + 1, remaining - using, containers[1:])
        if a[0] == b[0]:
            return a[0], a[1] + b[1]
        return min(a, b)
    else:
        return a


def main():
    containers = []
    with open('day17_input.txt') as f:
        for line in f:
            containers.append(int(line))

    print(allocate_ways(150, containers))
    print(min_allocate_ways(0, 150, containers))


if __name__ == "__main__":
    doctest.testmod()
    main()
