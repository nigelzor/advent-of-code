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

    # facing doesn't matter at the end node
    for direction in DIRECTIONS:
        g.add_edge((end, direction), end, weight=0)

    part1 = nx.shortest_path_length(g, (start, E), end, weight="weight")
    print(f"part 1: {part1}")

    good_seats = set()
    for path in nx.all_shortest_paths(g, (start, E), end, weight="weight"):
        for step in path[:-1]:
            good_seats.add(step[0])

    part2 = len(good_seats)
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
