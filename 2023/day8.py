import doctest
import itertools
import math
import re


def main():
    pattern = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")
    graph = dict()

    with open('day8_input.txt') as f:
        path = f.readline().strip()

        f.readline()

        for line in f:
            x, l, r = pattern.match(line).groups()
            graph[x] = (l, r)

    part1 = first_zzz(path, graph, "AAA")
    print(f"Part 1: {part1}")

    start_nodes = list(n for n in graph.keys() if n.endswith("A"))
    part2 = math.lcm(*[next(iterate_endswith_z(path, graph, n)) for n in start_nodes])
    print(f"Part 2: {part2}")


def first_zzz(path, graph, start: str):
    node = start
    for i, c in enumerate(itertools.cycle(path)):
        if node == "ZZZ":
            return i
        if c == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]


def iterate_endswith_z(path, graph, start: str):
    node = start
    for i, c in enumerate(itertools.cycle(path)):
        if node.endswith("Z"):
            yield i
        if c == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]


if __name__ == "__main__":
    doctest.testmod()
    main()
