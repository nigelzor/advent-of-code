import doctest
import re
from collections import defaultdict

p = re.compile(r'\d+ \w+')


def mid(a, b):
    if a == b:
        raise Exception('done')
    return a + ((b - a) // 2)


def parse(w):
    n, t = w.split(' ')
    return int(n), t


def main():
    ops = []
    # with open('day14_s.txt') as f:
    with open('day14_input.txt') as f:
        for line in f:
            inputs, outputs = line.strip().split(' => ')
            inputs = inputs.split(', ')
            ops.append((parse(outputs), tuple(parse(i) for i in inputs)))

    def subtract(d, t, n):
        if n == 0:
            return d
        dd = d.copy()
        dd[t] -= n
        return dd

    def add(d, t, n):
        if n == 0:
            return d
        dd = d.copy()
        dd[t] += n
        return dd

    def consume(d, t, n):
        c = d[t]
        if c > n:
            return 0, subtract(d, t, n)
        return n - c, subtract(d, t, c)

    # produce(need, excess) => (cost, excess)
    def produce(need, excess):
        # print('in', need, excess)
        n, t = need
        n, excess = consume(excess, t, n)
        if n == 0:
            return 0, excess
        if t == 'ORE':
            return n, excess
        for op in ops:
            (produce_n, produce_t), inputs = op
            if produce_t == t:
                cost = 0
                while n > 0:
                    for input in inputs:
                        sc, excess = produce(input, excess)
                        cost += sc
                    n -= produce_n
                if n < 0:
                    excess = add(excess, produce_t, -n)
                # print('out', cost, excess)
                return cost, excess



    total = produce((1, 'FUEL'), defaultdict(int))
    print(total[0])


if __name__ == "__main__":
    doctest.testmod()
    main()
