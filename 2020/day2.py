import doctest
import re


def valid_1(a, b, r, p):
    c = p.count(r)
    return a <= c <= b


def valid_2(a, b, r, p):
    is_a = p[a - 1] == r
    is_b = p[b - 1] == r
    return is_a + is_b == 1


def main():
    lines = []
    pattern = re.compile('^(\\d+)-(\\d+) (\\w): (.*)$')
    with open('day2_input.txt') as f:
        for line in f:
            a, b, r, p = pattern.match(line).groups()
            a = int(a)
            b = int(b)
            lines.append((a, b, r, p))

    print(sum(1 for line in lines if valid_1(*line)))
    print(sum(1 for line in lines if valid_2(*line)))


if __name__ == "__main__":
    doctest.testmod()
    main()
