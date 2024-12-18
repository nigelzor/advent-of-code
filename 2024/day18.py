import doctest
import networkx as nx


def main():
    falling = []

    with open("day18_input.txt") as f:
        for line in f:
            x, y = [int(v) for v in line.split(",")]
            falling.append((x, y))

    w = 70
    h = 70

    def part1():
        occupied = falling[:1024]
        g = nx.Graph()
        for x in range(w + 1):
            for y in range(h + 1):
                p = (x, y)
                if p in occupied:
                    continue
                if x > 0 and (x - 1, y) not in occupied:
                    g.add_edge(p, (x - 1, y))
                if y > 0 and (x, y - 1) not in occupied:
                    g.add_edge(p, (x, y - 1))
        return nx.shortest_path_length(g, (0, 0), (w, h))

    def part2():
        g = nx.Graph()
        for x in range(w + 1):
            for y in range(h + 1):
                p = (x, y)
                if x > 0:
                    g.add_edge(p, (x - 1, y))
                if y > 0:
                    g.add_edge(p, (x, y - 1))

        shortest_path = None
        for f in falling:
            g.remove_node(f)
            try:
                if not shortest_path or f in shortest_path:
                    shortest_path = nx.shortest_path(g, (0, 0), (w, h))
            except nx.NetworkXNoPath:
                return f"{f[0]},{f[1]}"

    print(f"part 1: {part1()}")
    print(f"part 2: {part2()}")


if __name__ == "__main__":
    doctest.testmod()
    main()
