import doctest


def Point(x, y):
    return x << 16 | y


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)


def main():
    start = None
    end = None
    grid = dict()

    with open('day23_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                p = Point(x, y)
                if c == '.':
                    if start is None:
                        start = p
                    end = p
                grid[p] = c

    pending_paths = [(start,)]
    found_paths = []

    while pending_paths:
        path = pending_paths.pop()

        for direction in [N, E, S, W]:
            next_step = path[-1] + direction
            if next_step == end:
                found_paths.append(path + (next_step,))
            else:
                ground = grid.get(next_step, '#')
                if ground == '#' or next_step in path:
                    continue
                if ground == '.' or (ground == '^' and direction == N) or (ground == '>' and direction == E) \
                        or (ground == 'v' and direction == S) or (ground == '<' and direction == W):
                    pending_paths.append(path + (next_step,))

    print(f"Part 1: {max(len(p) - 1 for p in found_paths)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
