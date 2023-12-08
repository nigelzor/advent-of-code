import doctest
import itertools
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

    node = 'AAA'
    for i, c in enumerate(itertools.cycle(path)):
        if node == "ZZZ":
            print(f"Part 1: {i}")
            break
        if c == "L":
            node = graph[node][0]
        else:
            node = graph[node][1]


if __name__ == "__main__":
    doctest.testmod()
    main()
