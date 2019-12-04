import doctest
from collections import defaultdict


def main():
    grid = defaultdict(bool)
    with open('day18_input.txt') as f:
        y = 0j
        for line in f:
            for x in range(0, 100):
                if line[x] == '#':
                    grid[x + y] = True
            y += 1j

    def count_neighbours(g, p):
        ns = [
            p - 1 - 1j, p - 1j, p + 1 - 1j,
            p - 1,              p + 1,
            p - 1 + 1j, p + 1j, p + 1 + 1j
        ]
        return sum(1 for n in ns if g[n])

    def next_state(g, p):
        ns = count_neighbours(g, p)
        if g[p]:
            return ns == 2 or ns == 3
        else:
            return ns == 3

    def next_grid(g):
        ng = defaultdict(bool)
        for y in range(100):
            for x in range(100):
                p = y * 1j + x
                if next_state(g, p):
                    ng[p] = True
        return ng

    g = grid
    for _ in range(100):
        g = next_grid(g)
    print(len(g))

    def always_on(g):
        g[0] = True
        g[99] = True
        g[99j] = True
        g[99+99j] = True

    g = grid
    always_on(g)
    for _ in range(100):
        g = next_grid(g)
        always_on(g)
    print(len(g))


if __name__ == "__main__":
    doctest.testmod()
    main()
