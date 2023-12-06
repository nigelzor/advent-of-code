import doctest
from collections import defaultdict


def part1(target, replacements):
    options = set()
    for a, bs in replacements.items():
        # print(f"{a} to {bs}:")
        at = 0
        while at >= 0:
            at = target.find(a, at)
            if at >= 0:
                for b in bs:
                    new = target[0:at] + b + target[at + len(a):]
                    options.add(new)
                at += 1
    return len(options)


def part2(target, replacements):
    inverted = defaultdict(list)
    for a, bs in replacements.items():
        for b in bs:
            inverted[b].append(a)
    print(inverted)


def main():
    replacements = defaultdict(list)
    with open('day19_input.txt') as f:
        for line in f:
            line = line.strip()
            if " => " in line:
                a, b = line.split(" => ")
                replacements[a].append(b)

    print(line)
    print(f"Part 1: {part1(line, replacements)}")
    print(f"Part 2: {part2(line, replacements)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
