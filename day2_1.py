from collections import defaultdict


def counts(input):
    """
    >>> counts("aa")
    {'a': 2}
    >>> counts("abc")
    {'a': 1, 'b': 1, 'c': 1}
    """
    cs = defaultdict(int)
    for c in input:
        cs[c] += 1
    return dict(cs)


def hasn(input, n):
    """
    >>> hasn("abc", 2)
    False
    >>> hasn("abbc", 2)
    True
    """
    return n in counts(input).values()


with open('day2.txt') as f:
    lines = [l.strip() for l in f.readlines()]
    twos = 0
    threes = 0
    for line in lines:
        c = counts(line)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1
    print('{} * {} = {}'.format(twos, threes, twos * threes))
