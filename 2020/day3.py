import doctest
from collections import defaultdict

OPEN = '.'
TREE = '#'


def main():
    map = defaultdict(lambda: OPEN)

    bottom = 0
    with open('day3_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                pos = x + y * 1j
                map[pos] = c
                bottom = pos

    def trees_hit(slope):
        pos = 0
        trees = 0
        while pos.imag <= bottom.imag:
            # print(pos, map[pos])
            if map[pos] == TREE:
                trees += 1

            pos += slope
            if pos.real > bottom.real:
                pos -= (bottom.real + 1)
        return trees

    print(trees_hit(3 + 1j))

    product = trees_hit(1 + 1j)
    product *= trees_hit(3 + 1j)
    product *= trees_hit(5 + 1j)
    product *= trees_hit(7 + 1j)
    product *= trees_hit(1 + 2j)
    print(product)


if __name__ == "__main__":
    doctest.testmod()
    main()
