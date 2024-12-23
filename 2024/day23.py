import doctest
import networkx as nx


def main():
    g = nx.Graph()
    with open("day23_input.txt") as f:
        for line in f:
            a, b = line.strip().split("-")
            g.add_edge(a, b)

    triples = list(c for c in nx.enumerate_all_cliques(g) if len(c) == 3)
    part1 = sum(1 for t in triples if any(c.startswith("t") for c in t))

    largest, _ = nx.max_weight_clique(g, weight=None)
    part2 = ",".join(sorted(largest))

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
