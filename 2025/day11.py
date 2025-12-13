import doctest
from functools import cache
import networkx as nx


def count_paths(g, start, end):
    # print(f"counting from {start} to {end}...")
    # return sum(1 for _ in nx.all_simple_edge_paths(g, start, end))

    @cache
    def _sum_in(g, n):
        if n == start:
            return 1
        return sum(_sum_in(g, pred) for pred in g.predecessors(n))

    return _sum_in(g, end)


def count_paths_through(g, nodes):
    ways = 1
    for src, dst in zip(nodes, nodes[1:]):
        ways *= count_paths(g, src, dst)
    return ways


def main():
    graph = nx.DiGraph()

    with open("day11_input.txt") as f:
        for line in f:
            device, outputs = line.strip().split(": ")
            outputs = outputs.split(" ")
            for output in outputs:
                graph.add_edge(device, output)

    part1 = count_paths(graph, "you", "out")
    print(f"part 1: {part1}")

    part2 = count_paths_through(
        graph, ["svr", "dac", "fft", "out"]
    ) + count_paths_through(graph, ["svr", "fft", "dac", "out"])
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
