import doctest
import networkx as nx

UP = -1j
DOWN = 1j
LEFT = -1
RIGHT = 1

DIRECTIONS = [UP, DOWN, LEFT, RIGHT]


def main():
    grid = dict()
    graph = nx.DiGraph()
    maxx = 0
    maxy = 0
    start = 0
    goal = 0

    with open('day12_input.txt') as f:
        for y, line in enumerate(f):
            if y > maxy:
                maxy = y
            line = line.rstrip()
            for x, h in enumerate(line):
                if x > maxx:
                    maxx = x
                pos = x + y * 1j
                if h == 'S':
                    start = pos
                    h = 'a'
                elif h == 'E':
                    goal = pos
                    h = 'z'
                grid[pos] = ord(h) - ord('a')

    for [pos, h] in grid.items():
        for d in DIRECTIONS:
            if pos + d in grid:
                dest_h = grid[pos + d]
                if dest_h <= h + 1:
                    graph.add_edge(pos, pos + d, weight=1)

    # for y in range(0, maxy + 1):
    #     for x in range(0, maxx + 1):
    #         print(grid[x + y * 1j], end=' ')
    #     print('')

    print(len(nx.shortest_path(graph, start, goal)) - 1)

    possible_starts = [pos for pos, h in grid.items() if h == 0 and nx.has_path(graph, pos, goal)]
    print(min(len(nx.shortest_path(graph, ps, goal)) - 1 for ps in possible_starts))


if __name__ == "__main__":
    doctest.testmod()
    main()
