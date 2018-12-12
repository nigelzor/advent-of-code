import re
from collections import defaultdict


def printstate(s):
    a = min(s.keys())
    z = max(s.keys())
    print(''.join([s[k] for k in range(a, z+1)]))

with open('day12.txt') as f:
    line = f.readline().strip().split(': ')[1]
    f.readline()

    state = defaultdict(lambda: '.')
    rules = defaultdict(lambda: '.')

    for i, c in enumerate(line):
        state[i] = c

    print('generation', 0)
    printstate(state)
    for line in f:
        pattern, output = line.strip().split(' => ')
        rules[pattern] = output

    for g in range(1, 20 + 1):
        newstate = defaultdict(lambda: '.')
        a = min(state.keys())
        z = max(state.keys())
        for k in range(a-2, z+3):
            key = ''.join([state[k - 2], state[k - 1], state[k], state[k + 1], state[k + 2]])
            next = rules[key]
            if next != '.':
                newstate[k] = next
        state = newstate
        print('generation', g)
        printstate(state)
        print(sum(k for k, v in state.items() if v == '#'))
