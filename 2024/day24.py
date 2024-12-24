import dataclasses
import doctest
from collections import deque
from functools import reduce


@dataclasses.dataclass
class Gate:
    inputs: set[str]
    output: str
    op: str

    @staticmethod
    def from_line(line):
        lhs, output = line.split(" -> ")
        a, op, b = lhs.split(" ")
        return Gate({a, b}, output, op)


def main():
    values = {}
    gates: deque[Gate] = deque()

    with open("day24_input.txt") as f:
        lines = (line.strip() for line in f)
        while line := next(lines):
            k, v = line.split(": ")
            values[k] = int(v)
        for line in lines:
            gates.append(Gate.from_line(line))

    bits = len(values) // 2
    xs = [f"x{i:02d}" for i in range(bits)]
    ys = [f"y{i:02d}" for i in range(bits)]
    zs = [f"z{i:02d}" for i in range(bits + 1)]

    def calculate(values):
        pending = gates.copy()
        while pending:
            g = pending.popleft()
            a, b = g.inputs
            if a in values and b in values:
                if g.op == "AND":
                    values[g.output] = values[a] and values[b]
                elif g.op == "OR":
                    values[g.output] = values[a] or values[b]
                elif g.op == "XOR":
                    values[g.output] = values[a] ^ values[b]
            else:
                pending.append(g)

        return reduce(
            lambda total, z: total * 2 + values[z],
            reversed(zs),
            0,
        )

    print(f"part 1: {calculate(values)}")

    def print_dot():
        print("digraph {")
        for g in gates:
            a, b = g.inputs
            print(f'{a} -> "{a} {g.op} {b}"')
            print(f'{b} -> "{a} {g.op} {b}"')
            print(f'"{a} {g.op} {b}" -> {g.output}')
        print("}")

    def calculate2(x, y):
        values = {}
        for xi, yi in zip(xs, ys):
            values[xi] = x & 1
            values[yi] = y & 1
            x //= 2
            y //= 2
        return calculate(values)

    def find_bad_z():
        bad = set()
        for i in range(bits):
            x = calculate2(0, 1 << i)
            y = calculate2(1 << i, 0)
            if x != 1 << i:
                bad.add(i)
            if y != 1 << i:
                bad.add(i)
        return bad

    swaps = [
        ("gmt", "z07"),
        ("cbj", "qjj"),
        ("dmn", "z18"),
        ("cfk", "z35"),
    ]

    for i, g in enumerate(gates):
        for swap in swaps:
            if g.output == swap[0]:
                gates[i] = dataclasses.replace(g, output=swap[1])
            elif g.output == swap[1]:
                gates[i] = dataclasses.replace(g, output=swap[0])

    def verify_after_swaps():
        def expect_gate(inputs, op):
            for g in gates:
                if g.inputs == inputs and g.op == op:
                    return g

        last_carry = None
        for i, (xi, yi) in enumerate(zip(xs, ys)):
            hi = expect_gate({xi, yi}, "AND")
            assert hi
            lo = expect_gate({xi, yi}, "XOR")
            assert lo

            if not last_carry:
                assert lo.output == zs[i]
                last_carry = hi
            else:
                out = expect_gate({last_carry.output, lo.output}, "XOR")
                assert out, f"missing out_{i}"
                assert (
                    out.output == zs[i]
                ), f"incorrect out_{i}: {out.output} should be {zs[i]}"
                carry_1 = expect_gate({last_carry.output, lo.output}, "AND")
                assert carry_1, f"missing carry_1_{i}"
                carry_2 = expect_gate({carry_1.output, hi.output}, "OR")
                assert carry_2, f"missing carry_2_{i}"
                last_carry = carry_2

    verify_after_swaps()

    print(f"part 2: {','.join(sorted(o for s in swaps for o in s))}")


if __name__ == "__main__":
    doctest.testmod()
    main()
