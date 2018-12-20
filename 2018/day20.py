import networkx as nx

DIRECTIONS = {
    'N': 1j,
    'E': 1,
    'W': -1,
    'S': -1j,
}

def travel(path):
    graph = nx.Graph()
    position = 0

    resume = []
    for c in path:
        if c == '(':
            resume.append(position)
        elif c == '|':
            position = resume[-1]
        elif c == ')':
            resume.pop()
        else:
            next_position = position + DIRECTIONS[c]
            graph.add_edge(position, next_position)
            position = next_position
    return graph

def longest(graph):
    source = 0
    dists, paths = nx.single_source_dijkstra(graph, source)
    return max(dists.values())

def long_paths(graph):
    source = 0
    dists, paths = nx.single_source_dijkstra(graph, source)
    return sum(1 for x in dists.values() if x >= 1000)


with open('day20.txt') as f:
    path = f.readline().strip()[1:-1]
    graph = travel(path)
    print('longest path', longest(graph))
    print('long paths', long_paths(graph))
