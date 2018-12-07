import re
from collections import defaultdict

p = re.compile('Step (.) must be finished before step (.) can begin\.')


with open('day7.txt') as f:
    all = set()
    inputs = defaultdict(set)
    avail = set()

    for line in f:
        req, step = p.match(line).groups()
        all.add(step)
        all.add(req)
        inputs[step].add(req)

    for k in all:
        if len(inputs[k]) == 0:
            avail.add(k)

    for k in avail:
        if k in inputs:
            del inputs[k]

    result = []
    while len(avail) > 0:
        current = min(avail)
        avail.remove(current)
        print('doing', current)
        result.append(current)

        for k in inputs.keys():
            inputs[k].discard(current)
            if len(inputs[k]) == 0:
                avail.add(k)

        for k in avail:
            if k in inputs:
                del inputs[k]

    print(''.join(result))
