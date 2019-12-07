from functools import lru_cache
from heapq import heappop, heappush
import networkx as nx

NEITHER = 1
GEAR = 2
TORCH = 4

ROCKY = 0
WET = 1
NARROW = 2

tools_allowed = dict()
tools_allowed[ROCKY] = GEAR | TORCH
tools_allowed[WET] = GEAR | NEITHER
tools_allowed[NARROW] = TORCH | NEITHER

depth = 11817
target = (9, 751, TORCH)
minx = 0
maxx = 300
miny = 0
maxy = 800

# depth = 510
# target = (10, 10, TORCH)
# minx = 0
# maxx = 20
# miny = 0
# maxy = 20


def erosion_level(x, y):
    return (geologic_index(x, y) + depth) % 20183


@lru_cache(maxsize=None)
def geologic_index(x, y):
    if x == 0 and y == 0:
        return 0
    if x == target[0] and y == target[1]:
        return 0
    if y == 0:
        return x * 16807
    if x == 0:
        return y * 48271
    return erosion_level(x - 1, y) * erosion_level(x, y - 1)


def region_type(x, y):
    return erosion_level(x, y) % 3


def risk(x, y):
    return region_type(x, y)


def options(x, y, tool):
    """
    >>> next(options(0, 0, TORCH))
    ((0, 0, 2), 7)
    """
    other_tool = tools_allowed[region_type(x, y)] & ~tool
    yield (x, y, other_tool), 7
    if x > minx and tools_allowed[region_type(x - 1, y)] & tool:
        yield (x - 1, y, tool), 1
    if x < maxx and tools_allowed[region_type(x + 1, y)] & tool:
        yield (x + 1, y, tool), 1
    if y > miny and tools_allowed[region_type(x, y - 1)] & tool:
        yield (x, y - 1, tool), 1
    if y < maxy and tools_allowed[region_type(x, y + 1)] & tool:
        yield (x, y + 1, tool), 1


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


if __name__ == '__main__':
    initial_position = (0, 0, TORCH)
    graph = nx.Graph()
    pending = []
    seen = set()
    heappush(pending, (0, initial_position))

    for i in range(1000):
        for _ in range(1000):
            if not pending:
                break
            t, position = heappop(pending)
            # print(t, position)
            for next_position, dt in options(*position):
                if graph.has_edge(position, next_position):
                    continue
                graph.add_edge(position, next_position, weight=dt)
                to_add = (t + dt, next_position)
                if to_add not in seen:
                    seen.add(to_add)
                    heappush(pending, to_add)

        if graph.has_node(target):
            print(i, graph.number_of_nodes(), nx.shortest_path_length(graph, initial_position, target, weight='weight'))
        else:
            print(i, graph.number_of_nodes(), 'Inf')
        if not pending:
            break




