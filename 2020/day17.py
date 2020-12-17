import doctest
from collections import defaultdict

INACTIVE = '.'
ACTIVE = '#'

ADJACENT = {(x, y, z, 0) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2)} - {(0, 0, 0, 0)}
assert len(ADJACENT) == 26

ADJACENT_2 = {(x, y, z, w) for x in range(-1, 2) for y in range(-1, 2) for z in range(-1, 2) for w in range(-1, 2)} - {(0, 0, 0, 0)}


def add_vec(a, b):
    return a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3]


def run_to_end(map, adjacency):
    for _ in range(6):
        next_map = dict()
        possible = defaultdict(int)
        for k, v in map.items():
            count = 0
            for a in adjacency(k):
                if map.get(a, INACTIVE) == ACTIVE:
                    count += 1
                else:
                    possible[a] += 1
            if count == 2 or count == 3:
                next_map[k] = ACTIVE
        for k, c in possible.items():
            if c == 3:
                next_map[k] = ACTIVE

        map = next_map
    print(len(map))


def main():
    map = dict()

    with open('day17_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                if c == ACTIVE:
                    pos = (x, y, 0, 0)
                    map[pos] = c

    def part1_adjacency(k):
        return (add_vec(k, a) for a in ADJACENT)
    run_to_end(map, part1_adjacency)

    def part2_adjacency(k):
        return (add_vec(k, a) for a in ADJACENT_2)
    run_to_end(map, part2_adjacency)


if __name__ == "__main__":
    doctest.testmod()
    main()
