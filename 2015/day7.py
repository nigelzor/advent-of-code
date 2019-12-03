import doctest
from functools import lru_cache


def main():
    wires = dict()

    @lru_cache(maxsize=None)
    def evaluate(wire):
        if wire.isnumeric():
            return int(wire)
        parts = wires[wire]
        if len(parts) == 1:
            src = parts[0]
            return evaluate(src)
        elif len(parts) == 2:
            op = parts[0]
            src = parts[1]
            if op == 'NOT':
                return ~evaluate(src)
            else:
                raise Exception("unhandled line", line)
        elif len(parts) == 3:
            op = parts[1]
            src = parts[0]
            arg = parts[2]
            if op == "AND":
                return evaluate(src) & evaluate(arg)
            elif op == "OR":
                return evaluate(src) | evaluate(arg)
            elif op == "LSHIFT":
                return evaluate(src) << evaluate(arg)
            elif op == "RSHIFT":
                return evaluate(src) >> evaluate(arg)
            else:
                raise Exception("unhandled line", line)

    with open('day7_input.txt') as f:
        for line in f:
            lhs, out = line.strip().split(' -> ')
            wires[out] = lhs.split(' ')


    initial_a = evaluate('a')
    print(initial_a)

    wires['b'] = [str(initial_a)]
    evaluate.cache_clear()
    print(evaluate('a'))


if __name__ == "__main__":
    doctest.testmod()
    main()
