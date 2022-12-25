import doctest


mapping = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
}

def snafu_to_decimal(s):
    """
    >>> snafu_to_decimal('1=-0-2')
    1747
    >>> snafu_to_decimal('1=-1=')
    353
    """
    value = []
    for c in s:
        value.append(mapping[c])
    return sum(5**exp * v for exp, v in enumerate(reversed(value)))


def decimal_to_snafu(v):
    """
    >>> decimal_to_snafu(1)
    '1'
    >>> decimal_to_snafu(2)
    '2'
    >>> decimal_to_snafu(3)
    '1='
    >>> decimal_to_snafu(4)
    '1-'
    >>> decimal_to_snafu(5)
    '10'
    >>> decimal_to_snafu(314159265)
    '1121-1110-1=0'
    """
    result = []
    while True:
        remainder = v % 5
        if remainder == 0:
            result.append('0')
        elif remainder == 1:
            result.append('1')
            v -= 1
        elif remainder == 2:
            result.append('2')
            v -= 2
        elif remainder == 3:
            result.append('=')
            v += 2
        elif remainder == 4:
            result.append('-')
            v += 1
        if not v:
            break
        v //= 5
    return ''.join(reversed(result))


def main():
    total = 0
    with open('day25_input.txt') as f:
        for line in f:
            total += snafu_to_decimal(line.strip())
    print(total)
    print(decimal_to_snafu(total))


if __name__ == "__main__":
    doctest.testmod()
    main()
