import doctest
from collections import defaultdict


def main():
    symbols = dict()
    parts = defaultdict(list)
    gears = defaultdict(list)

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
        for (start, length, val) in ps:
            def has_adjacent_symbol():
                result = False
                for yc in (y - 1j, y, y + 1j):
                    for xc in range(start - 1, start + length + 1):
                        s = symbols.get(xc + yc, None)
                        if s:
                            if s == '*':
                                gears[xc + yc].append(val)
                            result = True
                return result

            if has_adjacent_symbol():
                part1 += val

    print(f"Part 1: {part1}")

    part2 = 0
    for gear in gears.values():
        if len(gear) == 2:
            part2 += gear[0] * gear[1]
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
