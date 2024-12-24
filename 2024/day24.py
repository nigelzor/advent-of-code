import doctest
from collections import deque
from functools import reduce


def main():
    values = {}
    gates = deque()

    with open("day24_input.txt") as f:
        lines = (line.strip() for line in f)
        while line := next(lines):
            k, v = line.split(": ")
            values[k] = int(v)
        for line in lines:
            lhs, output = line.split(" -> ")
            a, op, b = lhs.split(" ")
            gates.append((a, op, b, output))

    while gates:
        g = gates.popleft()
        a, op, b, out = g
        if a in values and b in values:
            if op == "AND":
                values[out] = values[a] and values[b]
            elif op == "OR":
                values[out] = values[a] or values[b]
            elif op == "XOR":
                values[out] = values[a] ^ values[b]
        else:
            gates.append(g)

    def accumulate(total, item):
        return total * 2 + item[1]

    part1 = reduce(
        accumulate,
        sorted(((k, v) for k, v in values.items() if k.startswith("z")), reverse=True),
        0,
    )

    print(f"part 1: {part1}")


if __name__ == "__main__":
    doctest.testmod()
    main()
