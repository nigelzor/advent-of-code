import doctest
import networkx as nx
# import matplotlib.pyplot as plt


def Point(x, y):
    return x << 16 | y


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)


def contract(g):
    """
    Contract chains of neighbouring vertices with degree 2 into a single edge.

    adapted from https://stackoverflow.com/a/68500492
    """

    # create subgraph of all nodes with degree 2
    chain_nodes = [node for node, degree in g.degree() if degree == 2]
    chains = g.subgraph(chain_nodes)

    # contract connected components (which should be chains of variable length) into single node
    components = [chains.subgraph(c) for c in nx.connected_components(chains)]

    hyper_edges = []
    for component in components:
        end_points = [node for node, degree in component.degree() if degree < 2]
        candidates = set(neighbor for node in end_points for neighbor in g.neighbors(node))
        connectors = candidates - set(list(component.nodes()))
        hyper_edge = list(connectors)
        weight = sum(component.get_edge_data(*edge)['weight'] for edge in component.edges()) + 2
        hyper_edges.append((hyper_edge, weight))

    # initialise new graph with all other nodes
    not_chain = [node for node in g.nodes() if node not in chain_nodes]
    h = g.subgraph(not_chain).copy()
    for hyper_edge, weight in hyper_edges:
        h.add_edge(*hyper_edge, weight=weight)

    return h


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

    max_x = x
    max_y = y

    def part1():
        pending_paths = [(start,)]
        longest_path = 0

        while pending_paths:
            path = pending_paths.pop()

            for direction in [N, E, S, W]:
                next_step = path[-1] + direction
                if next_step == end:
                    longest_path = max(longest_path, len(path))
                else:
                    ground = grid.get(next_step, '#')
                    if ground == '#' or next_step in path:
                        continue
                    if ground == '.' \
                            or (ground == '^' and direction == N) \
                            or (ground == '>' and direction == E) \
                            or (ground == 'v' and direction == S) \
                            or (ground == '<' and direction == W):
                        pending_paths.append(path + (next_step,))
        return longest_path

    print(f"Part 1: {part1()}")

    def part2():
        graph = nx.Graph()
        for x in range(max_x + 1):
            for y in range(max_y + 1):
                p1 = Point(x, y)
                g1 = grid.get(p1, '#')
                for direction in [E, S]:
                    p2 = p1 + direction
                    g2 = grid.get(p2, '#')
                    if g1 != '#' and g2 != '#':
                        graph.add_edge(p1, p2, weight=1)

        graph = contract(graph)
        # nx.draw(graph)
        # plt.show()

        pending_paths = [(0, (start,))]
        longest_path = 0

        while pending_paths:
            weight, path = pending_paths.pop()
            position = path[-1]

            for next_step, data in graph.adj[position].items():
                if next_step in path:
                    continue

                next_weight = weight + data['weight']
                if next_step == end:
                    if next_weight > longest_path:
                        longest_path = next_weight
                else:
                    pending_paths.append((next_weight, path + (next_step,)))
        return longest_path

    print(f"Part 2: {part2()}")


if __name__ == "__main__":
    doctest.testmod()
    main()
