import doctest
from heapq import heappush, heappop
import networkx as nx


DIRECTIONS = {
    'D': 1j,
    'R': 1,
    'L': -1,
    'U': -1j,
}


def main(filename):
    maze = dict()
    with open(filename) as f:
        for y, line in enumerate(f):
            y *= 1j
            for x, c in enumerate(line.strip()):
                maze[x + y] = c

    keys = {v: k for k, v in maze.items() if v.islower()}
    doors = {v: k for k, v in maze.items() if v.isupper()}
    start = next(k for k, v in maze.items() if v == '@')
    # print(keys)
    # print(doors)
    # print(start)

    def is_open(v, opened=()):
        return v == '.' or v == '@' or v.islower() or v in opened

    graph = nx.Graph()
    for k, v in maze.items():
        if is_open(v):
            if is_open(maze.get(k + 1, '#')):
                graph.add_edge(k, k + 1)
            if is_open(maze.get(k + 1j, '#')):
                graph.add_edge(k, k + 1j)

    # (-len(opened), travelled, position, opened, graph)
    queue = []
    heappush(queue, (0, 0, start.real, start.imag, start, ()))
    best = None

    while queue:
        travelled, _, _, _, position, opened = heappop(queue)
        # print('expanding travelled:', travelled, 'opened:', opened, 'pending:', len(queue))
        if len(opened) == len(keys):
            if best is None or travelled < best:
                print('collected all keys in {} steps'.format(travelled))
                best = travelled
                break

        new_graph = graph.copy()
        for d in opened:
            if d in doors:
                door = doors[d]
                for x in DIRECTIONS.values():
                    if is_open(maze.get(door + x, '#'), opened):
                        new_graph.add_edge(door, door + x)

        for k in keys:
            d = k.upper()
            if d in opened:
                continue
            destination = keys[k]
            try:
                distance = nx.shortest_path_length(new_graph, position, destination)
            except nx.NetworkXNoPath:
                continue
            new_travelled = travelled + distance
            new_opened = (*opened, d)
            heappush(queue, (new_travelled, -len(opened), destination.real, destination.imag, destination, new_opened))


if __name__ == "__main__":
    doctest.testmod()
    # main('day18_s1.txt')
    # main('day18_s2.txt')
    # main('day18_s3.txt')
    # main('day18_s4.txt')
    main('day18_s5.txt')
    # main('day18_input.txt')  # 5194 is too high
