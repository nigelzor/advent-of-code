import doctest
from collections import defaultdict


def part1(tiles):
    options = defaultdict(set)
    for id, tile in tiles.items():
        for side in tile:
            options[side].add(id)
            options[side[::-1]].add(id)

    # print(len(tiles))  # 144 -- assuming 12x12
    outside = defaultdict(int)
    for ids in options.values():
        if len(ids) < 2:
            outside[next(iter(ids))] += 1
    # print(len(outside))  # 44 -- definitely 12x12

    corners = [id for id, n in outside.items() if n == 4]
    print(corners)
    prod = 1
    for c in corners:
        prod *= c
    print(prod)


def main():
    tiles = dict()
    id = None
    with open('day20_input.txt') as file:
        for line in file:
            line = line.strip()
            if not line:
                if id:
                    tiles[id] = (top, right, bottom, left)
            elif line.startswith('Tile '):
                id = int(line[5:-1])
                top = None
                left = ''
                right = ''
                bottom = None
            else:
                if not top:
                    top = line
                left += line[0]
                right += line[-1]
                bottom = line
    tiles[id] = (top, right, bottom, left)

    part1(tiles)


if __name__ == "__main__":
    doctest.testmod()
    main()
