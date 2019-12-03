import doctest
import networkx as nx
import re
from itertools import permutations


def main():
    p = re.compile(r'(\w+) to (\w+) = (\d+)')
    graph = nx.Graph()
    with open('day9_input.txt') as f:
        for line in f:
            a, b, dist = p.match(line).groups()
            graph.add_edge(a, b, weight=int(dist))


    def distance(path):
        prev = None
        total = 0
        for step in path:
            if prev:
                total += graph.get_edge_data(prev, step)['weight']
            prev = step
        return total

    options = [(distance(path), path) for path in permutations(graph.nodes)]
    print(min(options))
    print(max(options))


if __name__ == "__main__":
    doctest.testmod()
    main()
