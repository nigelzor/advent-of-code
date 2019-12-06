import doctest
import networkx as nx


def main():
    graph = nx.Graph()

    with open('day6_input.txt') as f:
        for line in f:
            l, r = line.strip().split(')')
            graph.add_edge(l, r)

    w = nx.single_source_shortest_path_length(graph, 'COM')
    total = 0
    for node in nx.nodes(graph):
        total += w[node]
    print(total)

    d = nx.shortest_path_length(graph, 'YOU', 'SAN')
    print(d - 2)


if __name__ == "__main__":
    doctest.testmod()
    main()
