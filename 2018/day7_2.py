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

    elves = 5
    work = [-1 for x in range(elves)]
    workitem = [None for x in range(elves)]
    time = 0

    result = []
    while len(avail) > 0 or max(work) > -1:
        print('time', time)

        for e in range(elves):
            if work[e] == 0:
                current = workitem[e]
                print('elf', e, 'finished', current)

                result.append(current)

                for k in inputs.keys():
                    inputs[k].discard(current)
                    if len(inputs[k]) == 0:
                        avail.add(k)

            for k in avail:
                if k in inputs:
                    del inputs[k]

        while len(avail):
            current = min(avail)
            duration = ord(current) - 64
            for e in range(elves):
                if work[e] < 1:
                    print('elf', e, 'doing', current, 'for', duration)
                    avail.remove(current)
                    work[e] = duration + 60
                    workitem[e] = current
                    break
            else:
                print('no worker available for', current)
                break

        time += 1
        for e in range(elves):
            work[e] -= 1

    print(''.join(result))
