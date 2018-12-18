from collections import defaultdict, Counter

OPEN = '.'
TREE = '|'
LUMBER = '#'


def load(filename):
    with open(filename) as f:
        board = defaultdict(lambda: OPEN)

        for y, line in enumerate(f):
            for x, c in enumerate(line):
                if c in (OPEN, TREE, LUMBER):
                    board[x, y] = c
                elif c not in " \n":
                    raise Exception('what is "{}"?'.format(c))
        return board


def print_board(board):
    for x in range(0, 50):
        print(''.join(board[x, y] for y in range(0, 50)))


def main():
    board = load('day18.txt')

    for minute in range(1000 + 1):
        lumberyards = len([x for x in board.values() if x == LUMBER])
        trees = len([x for x in board.values() if x == TREE])
        print('minute', minute, 'score', trees, lumberyards, '=', trees * lumberyards)
        # print_board(board)
        next_board = defaultdict(lambda: OPEN)
        for x in range(0, 50):
            for y in range(0, 50):
                adjacent = Counter([
                    board[x - 1, y - 1], board[x, y - 1], board[x + 1, y - 1],
                    board[x - 1, y], board[x + 1, y],
                    board[x - 1, y + 1], board[x, y + 1], board[x + 1, y + 1]
                ])
                if board[x, y] == OPEN:
                    if adjacent[TREE] >= 3:
                        next_board[x, y] = TREE
                    else:
                        next_board[x, y] = OPEN
                elif board[x, y] == TREE:
                    if adjacent[LUMBER] >= 3:
                        next_board[x, y] = LUMBER
                    else:
                        next_board[x, y] = TREE
                elif board[x, y] == LUMBER:
                    if adjacent[LUMBER] > 0 and adjacent[TREE] > 0:
                        next_board[x, y] = LUMBER
                    else:
                        next_board[x, y] = OPEN
        board = next_board


if __name__ == '__main__':
    main()
