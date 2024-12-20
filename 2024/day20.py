import doctest
from dataclasses import dataclass
import networkx as nx


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)

CHEATS = [
    Point(0, -2),
    Point(0, 2),
    Point(2, 0),
    Point(-2, 0),
]


def main():
    maze = dict()

    with open("day20_input.txt") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                p = Point(x, y)
                if c == "S":
                    # start = p
                    c = "."
                if c == "E":
                    end = p
                    c = "."
                maze[p] = c

    g = nx.Graph()
    for k, v in maze.items():
        if v == ".":
            for direction in (S, E):
                if maze[k + direction] == ".":
                    g.add_edge(k, k + direction, weight=1)

    distances = nx.single_source_dijkstra_path_length(g, end)

    part1 = 0
    for k, v in maze.items():
        if v == ".":
            for cheat in CHEATS:
                k2 = k + cheat
                if k2 in distances:
                    d = distances[k] - distances[k2] - 2
                    if d >= 100:
                        part1 += 1

    print(f"part 1: {part1}")


if __name__ == "__main__":
    doctest.testmod()
    main()
