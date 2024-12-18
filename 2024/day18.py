import doctest
import networkx as nx


def main():
    falling = []

    with open("day18_input.txt") as f:
        for line in f:
            x, y = [int(v) for v in line.split(",")]
            falling.append((x, y))

    occupied = falling[:1024]
    g = nx.Graph()
    w = 70
    h = 70

    for x in range(w + 1):
        for y in range(h + 1):
            p = (x, y)
            if p in occupied:
                continue
            if x < w and (x + 1, y) not in occupied:
                g.add_edge(p, (x + 1, y))
            if y < w and (x, y + 1) not in occupied:
                g.add_edge(p, (x, y + 1))

    part1 = nx.shortest_path_length(g, (0, 0), (w, h))
    print(f"part 1: {part1}")


if __name__ == "__main__":
    doctest.testmod()
    main()
