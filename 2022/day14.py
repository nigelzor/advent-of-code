import doctest


def coords_between(a, b):
    """
    >>> list(coords_between(0, 2))
    [0j, (1+0j), (2+0j)]
    """
    if a.real < b.real:
        return [r + a.imag * 1j for r in range(int(a.real), int(b.real) + 1)]
    if a.real > b.real:
        return [r + a.imag * 1j for r in range(int(b.real), int(a.real) + 1)]
    if a.imag < b.imag:
        return [a.real + r * 1j for r in range(int(a.imag), int(b.imag) + 1)]
    if a.imag > b.imag:
        return [a.real + r * 1j for r in range(int(b.imag), int(a.imag) + 1)]

def parse_line(line):
    for part in line.split(' -> '):
        x, y = [int(c) for c in part.split(',')]
        yield x + y * 1j


def print_grid(grid):
    minx = min(int(c.real) for c in grid.keys())
    maxx = max(int(c.real) for c in grid.keys())
    miny = min(int(c.imag) for c in grid.keys())
    maxy = max(int(c.imag) for c in grid.keys())

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            print(grid.get(x + y * 1j, '.'), end='')
        print('')


def main():
    grid = dict()

    with open('day14_input.txt') as f:
        for line in f:
            line = line.strip()
            coords = list(parse_line(line))
            for (a, b) in zip(coords, coords[1:]):
                for position in coords_between(a, b):
                    grid[position] = '#'

    start = 500+0j
    maxy = max(int(c.imag) for c in grid.keys())
    done = False

    while not done and grid.get(start, '.') == '.':
        position = start
        while True:
            if position.imag > maxy:
                print('falling off bottom')
                done = True
                break

            if grid.get(position + 1j, '.') == '.':
                position += 1j
            elif grid.get(position - 1 + 1j, '.') == '.':
                position += -1 + 1j
            elif grid.get(position + 1 + 1j, '.') == '.':
                position += 1 + 1j
            else:
                grid[position] = 'O'
                break

        # print_grid(grid)

    print(sum(1 for v in grid.values() if v == 'O'))



if __name__ == "__main__":
    doctest.testmod()
    main()
