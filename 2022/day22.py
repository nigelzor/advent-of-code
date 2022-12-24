import doctest
import re


WORD_BOUNDARY = re.compile(r'(?<=\d)(?=[A-Z])|(?=\d)(?<=[A-Z])')

LEFT_TURN = -1j
RIGHT_TURN = 1j

UP = -1j
DOWN = 1j
LEFT = -1
RIGHT = 1

FACING_RESULT = {
    RIGHT: 0,
    DOWN: 1,
    LEFT: 2,
    UP: 3,
}


def pt(x, y):
    return x + y * 1j

def main():
    grid = dict()

    with open('day22_input.txt') as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            if not line:
                break
            for x, c in enumerate(line):
                if c == '#' or c == '.':
                    grid[pt(x, y)] = c

        path = WORD_BOUNDARY.split(lines[-1].strip())
        for i, v in enumerate(path):
            if v.isnumeric():
                path[i] = int(v)

    def bounds():
        minx = min(int(c.real) for c in grid.keys())
        maxx = max(int(c.real) for c in grid.keys())
        miny = min(int(c.imag) for c in grid.keys())
        maxy = max(int(c.imag) for c in grid.keys())
        return minx, maxx, miny, maxy

    def print_grid():
        minx, maxx, miny, maxy = bounds()
        for y in range(miny, maxy + 1):
            for x in range(minx, maxx + 1):
                print(grid.get(pt(x, y), ' '), end='')
            print('')

    # print(path)
    # print_grid()

    position = pt(min(k.real for k, v in grid.items() if k.imag == 0 and v == '.'), 0)
    direction = 1+0j

    # sample:
    #   1
    # 234
    #   56
    edge_length = 4
    sides = [
                        (2, 0),
        (0, 1), (1, 1), (2, 1),
                        (2, 2), (3, 2),
    ]
    jumps = [ # from, direction, to, direction, flip?
        (1, UP, 5, UP, False),
        (2, UP, 1, DOWN, True),
        (3, UP, 1, RIGHT, False),
        (6, UP, 4, LEFT, True),
        (2, DOWN, 5, UP, True),
        (3, DOWN, 5, RIGHT, True),
        (5, DOWN, 2, UP, True),
        (6, DOWN, 2, RIGHT, True),
        (1, LEFT, 3, DOWN, False),
        (2, LEFT, 4, LEFT, False),
        (5, LEFT, 3, UP, True),
        (1, RIGHT, 6, LEFT, True),
        (4, RIGHT, 6, DOWN, True),
        (5, RIGHT, 3, UP, True),
    ]

    # mine:
    #  12
    #  3
    # 45
    # 6
    edge_length = 50
    sides = [
                (1, 0), (2, 0),
                (1, 1),
        (0, 2), (1, 2),
        (0, 3),
    ]
    jumps = [ # from, direction, to, direction, flip?
        (1, UP, 6, RIGHT, False),
        (2, UP, 6, UP, False),
        (4, UP, 3, RIGHT, False),
        (2, DOWN, 3, LEFT, False),
        (5, DOWN, 6, LEFT, False),
        (6, DOWN, 2, DOWN, False),
        (1, LEFT, 4, RIGHT, True),
        (3, LEFT, 4, DOWN, False),
        (4, LEFT, 1, RIGHT, True),
        (6, LEFT, 1, DOWN, False),
        (2, RIGHT, 5, LEFT, True),
        (3, RIGHT, 2, UP, False),
        (5, RIGHT, 2, LEFT, True),
        (6, RIGHT, 5, UP, False),
    ]

    def side_for(position):
        x = int(position.real) // edge_length
        y = int(position.imag) // edge_length
        return sides.index((x, y)) + 1  # 1-indexed

    for instruction in path:
        if instruction == 'L':
            direction *= LEFT_TURN
        elif instruction == 'R':
            direction *= RIGHT_TURN
        else:
            for _ in range(instruction):
                next_position = position + direction
                next_direction = direction
                at_next_position = grid.get(next_position, None)
                if at_next_position is None:
                    from_side = side_for(position)
                    jump = next(j for j in jumps if j[0] == from_side and j[1] == direction)
                    to_side = sides[jump[2] - 1]
                    print('nothing at', next_position, 'jumping from', from_side, jump[2])

                    if direction == UP or direction == DOWN:
                        offset = position.real % edge_length
                    else:
                        offset = position.imag % edge_length
                    if jump[4]:
                        offset = edge_length - offset - 1

                    next_direction = jump[3]
                    if next_direction == UP:
                        next_position = pt(to_side[0] * edge_length + offset, to_side[1] * edge_length + edge_length - 1)
                    elif next_direction == DOWN:
                        next_position = pt(to_side[0] * edge_length + offset, to_side[1] * edge_length)
                    elif next_direction == LEFT:
                        next_position = pt(to_side[0] * edge_length + edge_length - 1, to_side[1] * edge_length + offset)
                    else:
                        next_position = pt(to_side[0] * edge_length, to_side[1] * edge_length + offset)

                    print('now at', next_position)

                    at_next_position = grid.get(next_position, None)

                if at_next_position == '#':
                    break
                elif at_next_position == '.':
                    position = next_position
                    direction = next_direction
                else:
                    raise Exception('there should be something here')

    print(position, direction)
    print(1000 * int(position.imag + 1) + 4 * int(position.real + 1) + FACING_RESULT[direction])




if __name__ == "__main__":
    doctest.testmod()
    main()
