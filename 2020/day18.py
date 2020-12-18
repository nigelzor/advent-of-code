import doctest
import re


def calc1(line):
    """
    >>> calc1('2 * 3 + (4 * 5)')
    26
    >>> calc1('5 + (8 * 3 + 9 + 3 * 4 * 3)')
    437
    >>> calc1('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))')
    12240
    >>> calc1('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2')
    13632
    """
    while True:
        def calc_parens(match):
            return str(calc1(match.group(1)))
        line, n = re.subn(r'\(([^()]*)\)', calc_parens, line)
        if n:
            continue

        def calc_op(match):
            op = match.group(2)
            if op == '+':
                return str(int(match.group(1)) + int(match.group(3)))
            elif op == '*':
                return str(int(match.group(1)) * int(match.group(3)))
        line, n = re.subn(r'(\d+) ([+*]) (\d+)', calc_op, line, 1)
        if n:
            continue

        break
    return int(line)


def calc2(line):
    """
    >>> calc2('2 * 3 + (4 * 5)')
    46
    """
    while True:
        def calc_parens(match):
            return str(calc2(match.group(1)))
        line, n = re.subn(r'\(([^()]*)\)', calc_parens, line)
        if n:
            continue

        def calc_add(match):
            return str(int(match.group(1)) + int(match.group(2)))
        line, n = re.subn(r'(\d+) \+ (\d+)', calc_add, line)
        if n:
            continue

        def calc_mul(match):
            return str(int(match.group(1)) * int(match.group(2)))
        line, n = re.subn(r'(\d+) \* (\d+)', calc_mul, line)
        if n:
            continue

        break
    return int(line)


def main():
    total1 = 0
    total2 = 0

    with open('day18_input.txt') as file:
        for line in file:
            total1 += calc1(line.strip())
            total2 += calc2(line.strip())

    print(total1)
    print(total2)


if __name__ == "__main__":
    doctest.testmod()
    main()
