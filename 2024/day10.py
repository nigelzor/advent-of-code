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


def score(map, trailhead):
    visited = set()
    pending = {trailhead}
    while pending:
        current_position = pending.pop()
        current_height = map[current_position]
        visited.add(current_position)

        for direction in DIRECTIONS:
            next_position = current_position + direction
            next_height = map.get(next_position)
            if next_height is not None and (next_height - current_height) == 1:
                if next_position not in visited:
                    pending.add(next_position)

    return sum(1 for v in visited if map[v] == 9)


def part1(map):
    trailheads = {k for k, v in map.items() if v == 0}
    return sum(score(map, th) for th in trailheads)


def part2(map):
    g = nx.DiGraph()

    for position, height in map.items():
        for direction in DIRECTIONS:
            next_position = position + direction
            next_height = map.get(next_position)
            if next_height is not None and (next_height - height) == 1:
                g.add_edge(position, next_position)

    trailheads = {k for k, v in map.items() if v == 0}
    nines = {k for k, v in map.items() if v == 9}

    rating = 0
    for trailhead in trailheads:
        rating += sum(1 for _ in nx.all_simple_paths(g, trailhead, nines))
    return rating


def main():
    map = dict()

    with open("day10_input.txt") as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                if c != ".":
                    map[Point(x, y)] = int(c)

    print(f"part 1: {part1(map)}")
    print(f"part 2: {part2(map)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
