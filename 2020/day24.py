import doctest
from collections import defaultdict
import re

WHITE = False
BLACK = True

DIRECTIONS = {
    'e': (+1, -1, 0),
    'se': (0, -1, +1),
    'sw': (-1, 0, +1),
    'w': (-1, +1, 0),
    'nw': (0, +1, -1),
    'ne': (+1, 0, -1),
}


def steps(path):
    """
    >>> list(steps('nwwswee'))
    ['nw', 'w', 'sw', 'e', 'e']
    """
    for step in re.finditer(r'e|se|sw|w|nw|ne', path):
        yield step.group(0)


def main():
    board = defaultdict(lambda: WHITE)

    with open('day24_input.txt') as file:
        for line in file:
            x, y, z = 0, 0, 0
            for step in steps(line):
                dx, dy, dz = DIRECTIONS[step]
                x += dx
                y += dy
                z += dz
            board[(x, y, z)] = not board[(x, y, z)]

    print(sum(1 for v in board.values() if v is BLACK))

    for _ in range(100):
        black_neighbours = defaultdict(int)

        for k, v in board.items():
            x, y, z = k
            if v is BLACK:
                black_neighbours[k] += 0
                for dx, dy, dz in DIRECTIONS.values():
                    black_neighbours[(x + dx, y + dy, z + dz)] += 1

        for k, c in black_neighbours.items():
            if board[k] is BLACK:
                if c == 0 or c > 2:
                    del board[k]
            else:
                if c == 2:
                    board[k] = BLACK

    print(sum(1 for v in board.values() if v is BLACK))


if __name__ == "__main__":
    doctest.testmod()
    main()
