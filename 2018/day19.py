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
ops_by_name = { op.__name__: op for op in ops }

def load(filename):
    program = []
    with open(filename) as f:
        ipr = int(f.readline()[4:])
        for line in f.readlines():
            op, a, b, c = line.split(' ')
            program.append((op, int(a), int(b), int(c)))
    return ipr, program


def main():
    ipr, program = load('day19.txt')
    regs = [0 for _ in range(7)]

    while 0 <= regs[ipr] < len(program):
        inst = program[regs[ipr]]
        ops_by_name[inst[0]](regs, *inst[1:])
        regs[ipr] += 1
    print(regs)

if __name__ == '__main__':
    main()
