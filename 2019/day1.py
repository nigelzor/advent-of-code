import doctest
import math


def fuel_required(mass):
    """
    >>> fuel_required(12)
    2
    >>> fuel_required(14)
    2
    >>> fuel_required(1969)
    654
    >>> fuel_required(100756)
    33583
    """
    return max(math.floor(mass/3) - 2, 0)


def total_fuel_required(mass):
    """
    >>> total_fuel_required(14)
    2
    >>> total_fuel_required(1969)
    966
    >>> total_fuel_required(100756)
    50346
    """
    total = 0
    while mass > 0:
        fuel = fuel_required(mass)
        total += fuel
        mass = fuel
    return total


def main():
    modules = []
    with open('day1_input.txt') as f:
        for line in f:
            modules.append(int(line))

    print(sum(fuel_required(m) for m in modules))
    print(sum(total_fuel_required(m) for m in modules))


if __name__ == "__main__":
    doctest.testmod()
    main()
