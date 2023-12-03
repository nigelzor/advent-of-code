import doctest
from collections import defaultdict


def main():
    symbols = dict()
    # line -> (start, length, val)
    parts = defaultdict(list)

    with open('day3_input.txt') as f:
        y = 0
        for line in f:
            running = None
            for x, c in enumerate(line.strip()):
                if c.isdigit():
                    if running:
                        running += c
                    else:
                        running = c
                else:
                    if running:
                        parts[y].append((x - len(running), len(running), int(running)))
                    running = None
                    if c != '.':
                        symbols[x + y] = c
            if running:
                parts[y].append((x - len(running), len(running), int(running)))
            y += 1j

    part1 = 0
    for y, ps in parts.items():
        print(f"on line {y}")
        for part in ps:
            (start, length, val) = part
            print(f"part {val} at {start} ({length})", end='\t')

            def has_adjacent_symbol():
                for yc in (y - 1j, y, y + 1j):
                    for xc in range(start - 1, start + length + 1):
                        s = symbols.get(xc + yc, None)
                        if s:
                            print(f'found {s} at {xc + yc}')
                            return True
                return False

            if has_adjacent_symbol():
                part1 += val
            else:
                print(f'not found')
        # input()

    # too high 597755
    # too low  547476
    print(part1)


if __name__ == "__main__":
    doctest.testmod()
    main()
