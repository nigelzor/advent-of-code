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


def main(filename, recursive=False):
    maze = dict()
    with open(filename) as f:
        for y, line in enumerate(f):
            y *= 1j
            for x, c in enumerate(line.rstrip()):
                maze[x + y] = c

    xmin = min(k.real for k in maze.keys())
    xmax = max(k.real for k in maze.keys())
    ymin = min(k.imag for k in maze.keys())
    ymax = max(k.imag for k in maze.keys())

    def is_feature(v):
        return v.isupper()

    def portal_at(n):
        a = maze.get(n, ' ')
        if is_feature(a):
            outer = n.real <= xmin + 1 or n.real >= xmax - 1 or n.imag <= ymin + 1 or n.imag >= ymax - 1
            for d in DIRECTIONS.values():
                b = maze.get(n + d, ' ')
                if is_feature(b):
                    suffix = ''
                    if recursive:
                        suffix = '-' if outer else '+'
                    return ''.join(sorted([a, b])) + suffix
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

    def for_level(p, l):
        if p == 'AA-' or p == 'ZZ-':
            if l == 0:
                return p[:-1]
        elif p.endswith('-'):
            if l > 0:
                return p[:-1] + str(l)
        elif p.endswith('+'):
            return p[:-1] + str(l + 1)

    graph = nx.Graph()
    for k, v in maze.items():
        start = portal_at(k)
        if start:
            for o, d in neighbors(k).items():
                if recursive:
                    for level in range(100):
                        start_l = for_level(start, level)
                        end_l = for_level(o, level)
                        if start_l and end_l:
                            graph.add_edge(start_l, end_l, weight=d)
                else:
                    graph.add_edge(start, o, weight=d)

    # print(graph.edges)
    # pos = nx.spring_layout(graph, iterations=1000)
    # nx.draw(graph, pos, node_size=0, alpha=0.4, edge_color='r', font_size=16, with_labels=True)
    # nx.draw_networkx_edge_labels(graph, pos, edge_labels=nx.get_edge_attributes(graph, 'weight'))
    # plt.show()

    print(filename, 'recursive' if recursive else 'simple', nx.shortest_path_length(graph, 'AA', 'ZZ', weight='weight') - 1)


if __name__ == "__main__":
    doctest.testmod()
    main('day20_s1.txt')
    main('day20_s2.txt')
    main('day20_input.txt')
    main('day20_s1.txt', True)
    main('day20_s3.txt', True)
    main('day20_input.txt', True)
