import doctest

FLOOR = '.'
SEAT = 'L'
OCCUPIED = '#'

ADJACENT = {x + y * 1j for x in range(-1, 2) for y in range(-1, 2)} - {0}


def debug(map):
    print(f'{sum(1 for v in map.values() if v == OCCUPIED)}/{len(map)} seats occupied')
    maxx = max(int(x.real) for x in map.keys())
    maxy = max(int(x.imag) for x in map.keys())
    for y in range(0, maxy + 1):
        print(''.join(map.get(x + y * 1j, FLOOR) for x in range(0, maxx + 1)))


def run_to_end(map, adjacency, threshold):
    for _ in range(300):
        changed = False
        next_map = map.copy()
        for k, v in map.items():
            count = sum(1 for a in adjacency(k) if map.get(a, FLOOR) == OCCUPIED)
            if v == SEAT and count == 0:
                changed = True
                next_map[k] = OCCUPIED
            elif v == OCCUPIED and count >= threshold:
                changed = True
                next_map[k] = SEAT

        map = next_map
        # debug(map)

        if not changed:
            print(f'{sum(1 for v in map.values() if v == OCCUPIED)}/{len(map)} seats occupied')
            return


def main():
    map = dict()

    with open('day11_input.txt') as f:
        for y, line in enumerate(f):
            for x, c in enumerate(line.strip()):
                pos = x + y * 1j
                if c != FLOOR:
                    map[pos] = c

    maxx = max(int(x.real) for x in map.keys())
    maxy = max(int(x.imag) for x in map.keys())

    def part1_adjacency(k):
        return (k + a for a in ADJACENT)
    run_to_end(map, part1_adjacency, 4)

    def part2_adjacency(k):
        for direction in ADJACENT:
            p = k + direction
            while True:
                if p in map.keys():
                    yield p
                    break
                if p.real < 0 or p.real > maxx:
                    yield None
                    break
                if p.imag < 0 or p.imag > maxy:
                    yield None
                    break
                p += direction
    run_to_end(map, part2_adjacency, 5)


if __name__ == "__main__":
    doctest.testmod()
    main()
