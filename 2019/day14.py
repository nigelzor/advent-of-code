import doctest
import math
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
        d[t] -= n
        return d

    def add(d, t, n):
        d[t] += n
        return d

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
                mult = 1
                if n > produce_n:
                    mult = int(math.ceil(n / float(produce_n)))
                for in_n, in_t in inputs:
                    sc, excess = produce((in_n * mult, in_t), excess)
                    cost += sc
                extra = (produce_n * mult) - n
                excess = add(excess, produce_t, extra)
                # print('out', cost, excess)
                return cost, excess



    total = produce((1, 'FUEL'), defaultdict(int))
    print(total[0])


    limit = 1000000000000
    hi = 1024
    lo = 1

    n = hi
    while True:
        total = produce((n, 'FUEL'), defaultdict(int))[0]
        print(n, '=', total)
        if total < limit:
            lo = n
            if n == hi:
                n *= 2
                hi = n
            else:
                n = mid(lo, hi)
                if n == lo:
                    break
        elif total > limit:
            hi = n
            n = mid(lo, hi)


if __name__ == "__main__":
    doctest.testmod()
    main()
