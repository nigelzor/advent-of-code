import doctest
import re
import networkx as nx
from collections import defaultdict

line_pattern = re.compile('^(.*?) bags contain (.*)\\.$')
contents_pattern = re.compile('^(\\d+) (.*?) bags?$')


def parse_contents(contents: str):
    if contents == 'no other bags':
        return
    for c in contents.split(', '):
        count, name = contents_pattern.match(c).groups()
        yield int(count), name


def main():
    graph = nx.DiGraph()

    with open('day7_input.txt') as f:
        for line in f:
            bag, contents = line_pattern.match(line.strip()).groups()
            for c in parse_contents(contents):
                graph.add_edge(bag, c[1], weight=c[0])

    print(sum(1 for n in nx.ancestors(graph, 'shiny gold')))

    totals = defaultdict(int)
    pending = nx.descendants(graph, 'shiny gold') | {'shiny gold'}

    def process_pending(p):
        for c in graph[p]:
            if c in pending:
                return True  # can't process this one yet

        for c in graph[p]:
            weight = graph.edges[p, c]['weight']
            totals[p] += weight * (1 + totals[c])
        return False

    while pending:
        pending = [p for p in pending if process_pending(p)]

    print(totals['shiny gold'])


if __name__ == "__main__":
    doctest.testmod()
    main()
