import doctest
from os import path
from collections import defaultdict

def main():
    grid = dict()
    maxx = 0
    maxy = 0
    visible = set()

    with open('day8_input.txt') as f:
    # with open('day8_sample.txt') as f:
        for y, line in enumerate(f):
            if y > maxy:
                maxy = y
            line = line.rstrip()
            for x, h in enumerate(line):
                if x > maxx:
                    maxx = x
                grid[(x, y)] = int(h)

    for x in range(0, maxx + 1):
        maxh = -1
        for y in range(0, maxy + 1):
            h = grid[(x, y)]
            if h > maxh:
                maxh = h
                visible.add((x, y))
    for x in range(0, maxx + 1):
        maxh = -1
        for y in range(maxy, -1, -1):
            h = grid[(x, y)]
            if h > maxh:
                maxh = h
                visible.add((x, y))
    for y in range(0, maxy + 1):
        maxh = -1
        for x in range(0, maxx + 1):
            h = grid[(x, y)]
            if h > maxh:
                maxh = h
                visible.add((x, y))
    for y in range(0, maxy + 1):
        maxh = -1
        for x in range(maxx, -1, -1):
            h = grid[(x, y)]
            if h > maxh:
                maxh = h
                visible.add((x, y))

    # for y in range(0, maxy + 1):
    #     for x in range(0, maxx + 1):
    #         if (x, y) in visible:
    #             print('v', end='')
    #         else:
    #             print(' ', end='')
    #     print('')

    print(len(visible))


if __name__ == "__main__":
    doctest.testmod()
    main()
