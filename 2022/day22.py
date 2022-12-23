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
    # print(position, direction)

    for instruction in path:
        if instruction == 'L':
            direction *= LEFT_TURN
        elif instruction == 'R':
            direction *= RIGHT_TURN
        else:
            for _ in range(instruction):
                next_position = position + direction
                at_next_position = grid.get(next_position, None)
                if at_next_position is None:
                    opposite_direction = -direction
                    while next_position + opposite_direction in grid:
                        next_position = next_position + opposite_direction
                    at_next_position = grid.get(next_position, None)

                if at_next_position == '#':
                    break
                elif at_next_position == '.':
                    position = next_position

    print(position, direction)
    print(1000 * (position.imag + 1) + 4 * (position.real + 1) + FACING_RESULT[direction])





if __name__ == "__main__":
    doctest.testmod()
    main()
