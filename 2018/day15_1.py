import networkx as nx

OPEN = '.'
ELF = 'E'
GOBLIN = 'G'

class Elf:
    def __init__(self):
        self.health = 200

    def __str__(self):
        return ELF

class Goblin:
    def __init__(self):
        self.health = 200

    def __str__(self):
        return GOBLIN

def load(filename):
    with open(filename) as f:
        cave = dict()
        for y, line in enumerate(f):
            for x, c in enumerate(line):
                if c == OPEN:
                    cave[x, y] = OPEN
                elif c == ELF:
                    cave[x, y] = Elf()
                elif c == GOBLIN:
                    cave[x, y] = Goblin()

        return cave

def print_cave(cave):
    maxx = max(x for x, y in cave.keys())
    maxy = max(y for x, y in cave.keys())
    for y in range(0, maxy + 2):
        print(''.join(str(cave.get((x, y), '#')) for x in range(0, maxx + 2)))

def reading_order_key(item):
    return item[0][1], item[0][0]

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def adjacent_to(x, y):
    return [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]

def main():
    cave = load('day15.txt')

    def attack_adjacent(xy, char, targets):
        adjacent_targets = [(txy, tc) for txy, tc in targets if distance(xy, txy) == 1]
        if len(adjacent_targets):
            txy, tchar = min(adjacent_targets, key=lambda x: (x[1].health, reading_order_key(x)))
            tchar.health -= 3
            if tchar.health > 0:
                print(char, 'at', xy, 'attacks', tchar, 'at', txy, 'remaining health', tchar.health)
            else:
                print(char, 'at', xy, 'kills', tchar, 'at', txy)
                cave[txy] = OPEN
            return True

    def do_turn():
        turn_order = [item for item in cave.items() if item[1] != OPEN]
        turn_order.sort(key=reading_order_key)
        for xy, char in turn_order:
            if char not in cave.values():
                continue  # died this turn

            targets = [(txy, tc) for txy, tc in cave.items() if tc != OPEN and tc.__class__ != char.__class__]
            if len(targets) == 0:
                return True

            if attack_adjacent(xy, char, targets):
                continue

            graph = nx.Graph()
            maxx = max(x for x, y in cave.keys())
            maxy = max(y for x, y in cave.keys())
            for y in range(0, maxy + 1):
                for x in range(0, maxx + 1):
                    src = cave.get((x, y), '#')
                    dest = cave.get((x, y + 1), '#')
                    if (src == OPEN or src == char) and (dest == OPEN or dest == char):
                        graph.add_edge((x, y), (x, y + 1))
                    dest = cave.get((x + 1, y), '#')
                    if (src == OPEN or src == char) and (dest == OPEN or dest == char):
                        graph.add_edge((x, y), (x + 1, y))

            if xy in graph:
                potential_destinations = set()
                for txy, tchar in targets:
                    for axy in adjacent_to(*txy):
                        if cave.get(axy, '#') == OPEN:
                            potential_destinations.add(axy)

                distances = nx.multi_source_dijkstra_path_length(graph, {xy})
                connected_destinations = [(txy, distances[txy]) for txy in potential_destinations if txy in distances]
                if len(connected_destinations):
                    destination, dist = min(connected_destinations, key=lambda i: (i[1], i[0][1], i[0][0]))
                    # paths = nx.all_shortest_paths(graph, xy, destination)
                    # step = min((p[1] for p in paths), key=lambda x: (x[1], x[0]))
                    step = min((potential_step for potential_step in adjacent_to(*xy) if cave.get(potential_step, '#') == OPEN),
                               key=lambda s: nx.shortest_path_length(graph, s, destination))
                    print(char, 'at', xy, 'moves to', step, 'heading for', destination)
                    assert cave[step] == OPEN
                    cave[xy] = OPEN
                    cave[step] = char
                    attack_adjacent(step, char, targets)
                    continue

            print(char, 'at', xy, 'does nothing')

    for turn in range(0, 1000):
        print('turn', turn)
        if do_turn():
            print_cave(cave)
            remaining_hp = sum(i.health for i in cave.values() if i != OPEN)
            print('remaining hp', remaining_hp)
            print('answer', remaining_hp * turn)
            return


if __name__ == '__main__':
    main()
