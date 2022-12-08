import doctest

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
                grid[(x, y)] = int(h)

    def right_from(x, y):
        return ((x2, y) for x2 in range(x + 1, maxx + 1))
    def left_from(x, y):
        return ((x2, y) for x2 in range(x - 1, -1, -1))
    def up_from(x, y):
        return ((x, y2) for y2 in range(y - 1, -1, -1))
    def down_from(x, y):
        return ((x, y2) for y2 in range(y + 1, maxy + 1))

    visible = set()
    def collect_visible(edge, direction):
        for (x, y) in edge:
            maxh = -1
            for position in direction(x, y):
                h = grid[position]
                if h > maxh:
                    maxh = h
                    visible.add(position)

    top_edge = ((x, -1) for x in range(0, maxx + 1))
    bottom_edge = ((x, maxy + 1) for x in range(0, maxx + 1))
    left_edge = ((-1, y) for y in range(0, maxy + 1))
    right_edge = ((maxx + 1, y) for y in range(0, maxy + 1))

    collect_visible(top_edge, down_from)
    collect_visible(bottom_edge, up_from)
    collect_visible(left_edge, right_from)
    collect_visible(right_edge, left_from)

    # for y in range(0, maxy + 1):
    #     for x in range(0, maxx + 1):
    #         if (x, y) in visible:
    #             print('v', end='')
    #         else:
    #             print(' ', end='')
    #     print('')

    print(len(visible))

    def scenic_score(x, y):
        treehouse_height = grid[(x, y)]
        s = 1
        for direction in [right_from, left_from, up_from, down_from]:
            visible = 0
            for position in direction(x, y):
                tree_height = grid[position]
                visible += 1
                if tree_height >= treehouse_height:
                    break
            s *= visible
        return s

    print(max(scenic_score(x, y) for x in range(0, maxx + 1) for y in range(0, maxy + 1)))


if __name__ == "__main__":
    doctest.testmod()
    main()
