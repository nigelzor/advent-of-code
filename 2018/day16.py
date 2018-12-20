import re

def addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]
def addi(regs, a, b, c):
    regs[c] = regs[a] + b
def mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]
def muli(regs, a, b, c):
    regs[c] = regs[a] * b
def banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]
def bani(regs, a, b, c):
    regs[c] = regs[a] & b
def borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]
def bori(regs, a, b, c):
    regs[c] = regs[a] | b
def setr(regs, a, b, c):
    regs[c] = regs[a]
def seti(regs, a, b, c):
    regs[c] = a
def gtir(regs, a, b, c):
    regs[c] = 1 if a > regs[b] else 0
def gtri(regs, a, b, c):
    regs[c] = 1 if regs[a] > b else 0
def gtrr(regs, a, b, c):
    regs[c] = 1 if regs[a] > regs[b] else 0
def eqir(regs, a, b, c):
    regs[c] = 1 if a == regs[b] else 0
def eqri(regs, a, b, c):
    regs[c] = 1 if regs[a] == b else 0
def eqrr(regs, a, b, c):
    regs[c] = 1 if regs[a] == regs[b] else 0


ops = [addr,
       addi,
       mulr,
       muli,
       banr,
       bani,
       borr,
       bori,
       setr,
       seti,
       gtir,
       gtri,
       gtrr,
       eqir,
       eqri,
       eqrr]


def numbers(line):
    clean = re.sub(r'[^0-9 ]', '', line).strip()
    return [int(x) for x in clean.split(' ')]


def load(filename):
    samples = []

    with open(filename) as f:
        while True:
            line = f.readline()
            if line.startswith('Before'):
                before = numbers(line.split(': ')[1])
            else:
                break
            instruction = numbers(f.readline())
            after = numbers(f.readline().split(': ')[1])
            f.readline()
            samples.append((before, instruction, after))

        f.readline()
        program = [numbers(l) for l in f.readlines()]

    return samples, program


def main():
    samples, program = load('day16.txt')

    def matches(op, before, instruction, after):
        regs = before.copy()
        op(regs, *instruction[1:])
        return regs == after

    def possible(before, instruction, after):
        return [op for op in ops if matches(op, before, instruction, after)]

    print('Part 1:', sum(1 for sample in samples if len(possible(*sample)) >= 3))

    all_opcodes = set(range(0, 16))
    possible_opcodes = {}
    for oc in all_opcodes:
        possible_opcodes[oc] = set(o for o in ops)

    for sample in samples:
        oc = sample[1][0]
        ps = possible(*sample)
        possible_opcodes[oc] &= set(o for o in ps)

    defined = set()
    while True:
        changed = False
        for oc in all_opcodes - defined:
            if len(possible_opcodes[oc]) == 1:
                defined.add(oc)
                definitely = next(iter(possible_opcodes[oc]))
                # print(oc, 'is definitely', definitely.__name__)
                for ooc in all_opcodes - defined:
                    if definitely in possible_opcodes[ooc]:
                        changed = True
                        possible_opcodes[ooc].remove(definitely)
        if not changed:
            break

    opcodes = { k: next(iter(v)) for k, v in possible_opcodes.items() }
    print(opcodes)

    regs = [0, 0, 0, 0]
    for instruction in program:
        opcodes[instruction[0]](regs, *instruction[1:])
    print('Part 2:', regs)


if __name__ == '__main__':
    main()
