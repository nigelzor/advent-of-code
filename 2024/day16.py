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

DIRECTIONS = (N, S, E, W)

turn_right = {N: E, E: S, S: W, W: N}
turn_left = {N: W, E: N, S: E, W: S}


def main():
    maze = dict()

    with open("day16_input.txt") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                p = Point(x, y)
                if c == "S":
                    start = p
                    c = "."
                if c == "E":
                    end = p
                    c = "."
                maze[p] = c

    g = nx.DiGraph()
    for k, v in maze.items():
        if v == ".":
            for direction in DIRECTIONS:
                if maze[k + direction] == ".":
                    g.add_edge((k, direction), (k + direction, direction), weight=1)

                g.add_edge((k, direction), (k, turn_left[direction]), weight=1000)
                g.add_edge((k, direction), (k, turn_right[direction]), weight=1000)

    part1 = min(
        nx.shortest_path_length(g, (start, E), (end, direction), weight="weight")
        for direction in DIRECTIONS
    )

    print(f"part 1: {part1}")


if __name__ == "__main__":
    doctest.testmod()
    main()
