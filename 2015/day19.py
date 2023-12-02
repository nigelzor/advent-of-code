import doctest
from collections import defaultdict


def main():
    replacements = defaultdict(list)
    with open('day19_input.txt') as f:
        for line in f:
            line = line.strip()
            if " => " in line:
                a, b = line.split(" => ")
                replacements[a].append(b)

    print(line)

    options = set()
    for a, bs in replacements.items():
        print(f"{a} to {bs}:")
        at = 0
        while at >= 0:
            at = line.find(a, at)
            if at >= 0:
                for b in bs:
                    newline = line[0:at] + b + line[at + len(a):]
                    options.add(newline)
                at += 1

    print(len(options))


if __name__ == "__main__":
    doctest.testmod()
    main()
