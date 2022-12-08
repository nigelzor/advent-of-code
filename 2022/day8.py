import doctest

UP = -1j
DOWN = 1j
LEFT = -1
RIGHT = 1

def main():
    grid = dict()
    maxx = 0
    maxy = 0

    with open('day8_input.txt') as f:
        for y, line in enumerate(f):
            if y > maxy:
                maxy = y
            line = line.rstrip()
            for x, h in enumerate(line):
                if x > maxx:
                    maxx = x
                grid[x + y * 1j] = int(h)

    def travel(start, direction, inclusive=True):
        position = start
        if not inclusive:
            position += direction
        while position in grid:
            yield position
            position += direction

    visible = set()
    def collect_visible(edge, direction):
        for start in edge:
            maxh = -1
            for position in travel(start, direction):
                h = grid[position]
                if h > maxh:
                    maxh = h
                    visible.add(position)

    top_edge = travel(0, RIGHT)
    bottom_edge = travel(maxy * 1j, RIGHT)
    left_edge = travel(0, DOWN)
    right_edge = travel(maxx, DOWN)

    collect_visible(top_edge, DOWN)
    collect_visible(bottom_edge, UP)
    collect_visible(left_edge, RIGHT)
    collect_visible(right_edge, LEFT)

    # for y in range(0, maxy + 1):
    #     for x in range(0, maxx + 1):
    #         if (x + y * 1j) in visible:
    #             print('v', end='')
    #         else:
    #             print(' ', end='')
    #     print('')

    print(len(visible))

    def scenic_score(start):
        treehouse_height = grid[start]
        s = 1
        for direction in [UP, DOWN, LEFT, RIGHT]:
            visible = 0
            for position in travel(start, direction, inclusive=False):
                tree_height = grid[position]
                visible += 1
                if tree_height >= treehouse_height:
                    break
            s *= visible
        return s

    print(max(scenic_score(p) for p in grid.keys()))


if __name__ == "__main__":
    doctest.testmod()
    main()
