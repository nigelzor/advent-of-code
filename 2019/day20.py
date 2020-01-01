import doctest
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


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
            for x, c in enumerate(line.rstrip()):
                maze[x + y] = c

    def is_feature(v):
        return v.isupper()

    def portal_at(n):
        a = maze.get(n, ' ')
        if is_feature(a):
            for d in DIRECTIONS.values():
                b = maze.get(n + d, ' ')
                if is_feature(b):
                    return ''.join(sorted([a, b]))
        return None

    def neighbors(n):
        start = portal_at(n)
        distances = dict()
        pending = deque()
        pending.append((n, 0))
        while pending:
            x, distance = pending.popleft()
            if x in distances:
                continue
            distances[x] = distance
            if x == n or  maze.get(x, '#') == '.':
                for d in DIRECTIONS.values():
                    pending.append((x + d, distance + 1))
        r = {portal_at(k): d - 1 for k, d in distances.items() if portal_at(k) and portal_at(k) != start}
        # print(n, r)
        return r

    graph = nx.Graph()
    for k, v in maze.items():
        start = portal_at(k)
        if start:
            for o, d in neighbors(k).items():
                graph.add_edge(start, o, weight=d)

    print(nx.shortest_path(graph, 'AA', 'ZZ', weight='weight'))
    print(nx.shortest_path_length(graph, 'AA', 'ZZ', weight='weight') - 1)

    pos = nx.spring_layout(graph, iterations=1000)
    nx.draw(graph, pos, node_size=0, alpha=0.4, edge_color='r', font_size=16, with_labels=True)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, 'weight'))
    plt.show()


if __name__ == "__main__":
    doctest.testmod()
    main('day20_s1.txt')
    main('day20_s2.txt')
    main('day20_input.txt')
