from collections import defaultdict
import sys

sys.setrecursionlimit(2**16)

CLAY = '#'
SAND = '.'
FLOW = '|'
STILL = '~'


def load(filename):
    with open(filename) as f:
        board = defaultdict(lambda: SAND)

        for line in f:
            c0, c1 = line.split(', ')
            c0n, c0v = c0.split('=')
            c1n, c1v = c1.split('=')
            c1min, c1max = c1v.split('..')

            if c0n == 'x':
                for y in range(int(c1min), int(c1max) + 1):
                    board[int(c0v), y] = CLAY
            elif c0n == 'y':
                for x in range(int(c1min), int(c1max) + 1):
                    board[x, int(c0v)] = CLAY
            else:
                raise Exception('what?')

        return board


def limits(board):
    minx = None
    maxx = None
    miny = None
    maxy = None
    for x, y in board.keys():
        if minx is None or x < minx:
            minx = x
        if maxx is None or x > maxx:
            maxx = x
        if miny is None or y < miny:
            miny = y
        if maxy is None or y > maxy:
            maxy = y
    return minx - 1, maxx + 1, miny, maxy


def main():
    board = load('day17.txt')
    minx, maxx, miny, maxy = limits(board)

    # maxy = 26

    def print_board():
        for y in range(0, maxy + 1):
            print(''.join(board[x, y] for x in range(minx, maxx + 1)))

    # print('initial:')
    # print_board()

    def advance_flow(x, y, d=None):
        if y > maxy:
            return FLOW
        assert board[x, y] == SAND
        board[x, y] = FLOW
        # print('advance_flow', x, y)
        # print_board()
        if board[x, y + 1] == FLOW:
            return FLOW
        if board[x, y + 1] == SAND:
            if advance_flow(x, y + 1) == FLOW:
                return FLOW

        if d == 'left' and board[x - 1, y] == FLOW:
            return FLOW
        if d == 'right' and board[x + 1, y] == FLOW:
            return FLOW

        left = None
        right = None
        if board[x - 1, y] == SAND:
            left = advance_flow(x - 1, y, 'left')
        if board[x + 1, y] == SAND:
            right = advance_flow(x + 1, y, 'right')
        if left == FLOW or right == FLOW:
            return FLOW
        else:
            if not d:
                xl = x - 1
                while board[xl, y] == FLOW:
                    board[xl, y] = STILL
                    xl -= 1
                xr = x + 1
                while board[xr, y] == FLOW:
                    board[xr, y] = STILL
                    xr += 1
                board[x, y] = STILL
            return STILL

    advance_flow(500, 0)

    print('done:')
    print_board()
    print('part 1:', len([v for (x, y), v in board.items() if y >= miny and (v == FLOW or v == STILL)]))
    print('part 2:', len([v for (x, y), v in board.items() if y >= miny and v == STILL]))


if __name__ == '__main__':
    main()
    # 44747 is high
