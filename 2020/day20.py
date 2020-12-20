import doctest
from collections import defaultdict, namedtuple

TOP = 0
RIGHT = 1
BOTTOM = 2
LEFT = 3

POSSIBLE_ROTATIONS = [(r, f) for f in [False, True] for r in range(4)]

SNEK = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""[1:-1].split('\n')


class Tile:
    def __init__(self):
        self.lines = []
        self.top = ''
        self.right = ''
        self.bottom = ''
        self.left = ''

    def add_line(self, line):
        self.lines.append(line)
        if not self.top:
            self.top = line
        self.left += line[0]
        self.right += line[-1]
        self.bottom = line

    def sides(self, rotate=0, flip=False):
        if flip:
            s = (self.top[::-1], self.left, self.bottom[::-1], self.right)
        else:
            s = (self.top, self.right, self.bottom, self.left)
        for _ in range(rotate):
            s = (s[LEFT][::-1], s[TOP], s[RIGHT][::-1], s[BOTTOM])
        return s


def flip_lines(lines: list[str]):
    """
    >>> flip_lines(['ab', 'cd'])
    ['ba', 'dc']
    """
    return [line[::-1] for line in lines]


def rotate_lines(lines: list[str], rotate):
    """
    >>> rotate_lines(['ab', 'cd'], 1)
    ['ca', 'db']
    >>> rotate_lines(['abc', 'def'], 1)
    ['da', 'eb', 'fc']
    """
    if rotate >= 2:
        rotate -= 2
        lines = [line[::-1] for line in reversed(lines)]
    if rotate >= 1:
        rotate -= 1
        lines = [''.join(lines[x][y] for x in range(len(lines)))[::-1] for y in range(len(lines[0]))]
    return lines


class Assignment(namedtuple('Assignment', ['tile', 'rotate', 'flip'])):
    def sides(self, tiles: dict[int, Tile]):
        return tiles[self.tile].sides(self.rotate, self.flip)

    def content(self, tiles: dict[int, Tile]):
        tile = tiles[self.tile]
        lines = [line[1:-1] for line in tile.lines[1:-1]]
        if self.flip:
            lines = flip_lines(lines)
        return rotate_lines(lines, self.rotate)


def categorize_tiles(tiles: dict[int, Tile]):
    options = defaultdict(set)
    for id, tile in tiles.items():
        for side in tile.sides():
            options[side].add(id)
            options[side[::-1]].add(id)

    outside = defaultdict(int)
    for ids in options.values():
        if len(ids) < 2:
            outside[next(iter(ids))] += 1

    corners = {id for id, n in outside.items() if n == 4}
    assert len(corners) == 4
    edges = {id for id, n in outside.items() if n == 2}
    assert len(edges) == 40
    middle = set(tiles.keys()) - corners - edges
    assert len(middle) == 100

    return options, corners, edges, middle


def part1(tiles: dict[int, Tile]):
    options, corners, edges, middle = categorize_tiles(tiles)
    print(corners)
    prod = 1
    for c in corners:
        prod *= c
    print(prod)


def part2(tiles: dict[int, Tile]):
    options, corners, edges, middle = categorize_tiles(tiles)

    def tile_options_at(k: complex):
        if k in (0, 11, 0 + 11j, 11 + 11j):
            return corners
        if k.real == 0 or k.real == 11 or k.imag == 0 or k.imag == 11:
            return edges
        return middle

    def assignment_options_at(board: dict[complex, Assignment], k: complex):
        possible_tiles = tile_options_at(k) - {a.tile for a in board.values()}
        required_top = None
        required_left = None
        if k.imag > 0:
            required_top = board[k - 1j].sides(tiles)[BOTTOM]
            possible_tiles &= options[required_top]
        if k.real > 0:
            required_left = board[k - 1].sides(tiles)[RIGHT]
            possible_tiles &= options[required_left]
        for tile in possible_tiles:
            for r, f in POSSIBLE_ROTATIONS:
                a = Assignment(tile, r, f)
                sides = a.sides(tiles)
                if required_top and sides[TOP] != required_top:
                    continue
                if required_left and sides[LEFT] != required_left:
                    continue
                yield a

    indexes = [x + y * 1j for y in range(12) for x in range(12)]

    def assign_all(board: dict[complex, Assignment], at: int):
        if at == len(indexes):
            return board
        k = indexes[at]
        for ao in assignment_options_at(board, k):
            new_board = board.copy()
            new_board[k] = ao
            result = assign_all(new_board, at + 1)
            if result:
                return result

    solved = assign_all(dict(), 0)
    content = dict()
    for k, a in solved.items():
        tile_content = a.content(tiles)
        assert len(tile_content) == 8
        for y, tile_row in enumerate(tile_content):
            for x, v in enumerate(tile_row):
                ck = (8 * k) + y * 1j + x
                content[ck] = v

    found = False
    for r, f in POSSIBLE_ROTATIONS:
        lines = SNEK
        if f:
            lines = flip_lines(lines)
        lines = rotate_lines(lines, r)
        snek = {x + y * 1j for y in range(len(lines)) for x in range(len(lines[0])) if lines[y][x] == '#'}

        for y in range(96):
            for x in range(96):
                if all(content.get(x + y * 1j + c, None) == '#' for c in snek):
                    found = True
                    for c in snek:
                        content[x + y * 1j + c] = 'O'
        if found:
            break

    for y in range(96):
        print(''.join(content[x + y * 1j] for x in range(96)))
    print(sum(1 for v in content.values() if v == '#'))


def main():
    tiles = dict()
    with open('day20_input.txt') as file:
        for line in file:
            line = line.strip()
            if not line:
                pass
            elif line.startswith('Tile '):
                id = int(line[5:-1])
                tile = Tile()
                tiles[id] = tile
            else:
                tile.add_line(line)

    part1(tiles)
    part2(tiles)


if __name__ == "__main__":
    doctest.testmod()
    main()
