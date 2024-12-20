import doctest
from collections import defaultdict
from dataclasses import dataclass
import networkx as nx


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def duration(self):
        return abs(self.x) + abs(self.y)


N = Point(0, -1)
S = Point(0, 1)
E = Point(1, 0)
W = Point(-1, 0)

PART1_CHEATS = [
    Point(0, -2),
    Point(0, 2),
    Point(2, 0),
    Point(-2, 0),
]

PART2_CHEATS = [
    Point(x, y) for x in range(-20, 21) for y in range(-20 + abs(x), 21 - abs(x))
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

    def count_good_cheats(allowed, threshold=100):
        counts = defaultdict(int)
        for k, v in maze.items():
            if v == ".":
                for cheat in allowed:
                    k2 = k + cheat
                    if k2 in distances:
                        saved = distances[k] - distances[k2] - cheat.duration()
                        if saved >= threshold:
                            counts[saved] += 1
        return sum(counts.values())

    print(f"part 1: {count_good_cheats(PART1_CHEATS)}")
    print(f"part 2: {count_good_cheats(PART2_CHEATS)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
