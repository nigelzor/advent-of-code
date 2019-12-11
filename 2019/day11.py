import doctest
import itertools


def decode(intcode):
    """
    >>> decode(1002)
    (2, 0, 1, 0)
    >>> decode(1108)
    (8, 1, 1, 0)
    """
    op = intcode % 100
    modes = intcode // 100
    mode_c = modes % 10
    modes = modes // 10
    mode_b = modes % 10
    modes = modes // 10
    mode_a = modes % 10
    return op, mode_c, mode_b, mode_a


class Simulator:
    def __init__(self, program, inputs=None):
        self.program = program
        self.program.extend(0 for _ in range(1000))
        self.ip = 0
        self.rb = 0
        self.inputs = iter(inputs or [])

    def run_to_completion(self, inputs=None):
        if inputs:
            self.inputs = itertools.chain(self.inputs, inputs)
        outputs = []
        while True:
            out = self.simulate()
            if out is None:
                break
            outputs.append(out)
        return outputs

    def run_to_output(self, inputs=None):
        if inputs:
            self.inputs = itertools.chain(self.inputs, inputs)
        return self.simulate()

    def simulate(self):
        while True:
            inst = decode(self.program[self.ip])
            op = inst[0]

            # print('ip={} inst={}'.format(ip, inst))
            def in_arg(n):
                value = self.program[self.ip + n]
                mode = inst[n]
                if mode == 0:
                    return self.program[value]
                elif mode == 1:
                    return value
                elif mode == 2:
                    return self.program[value + self.rb]
                else:
                    raise Exception("Invalid mode {} at {}:{}".format(mode, self.ip, self.program[self.ip]))

            def out_arg(n, value):
                mode = inst[n]
                addr = self.program[self.ip + n]
                if mode == 0:
                    self.program[addr] = value
                elif mode == 2:
                    self.program[addr + self.rb] = value
                else:
                    raise Exception("Invalid mode {} at {}:{}".format(mode, self.ip, self.program[self.ip]))

            if op == 1:
                a = in_arg(1)
                b = in_arg(2)
                out_arg(3, a + b)
                self.ip += 4
            elif op == 2:
                a = in_arg(1)
                b = in_arg(2)
                out_arg(3, a * b)
                self.ip += 4
            elif op == 3:
                out_arg(1, next(self.inputs))
                self.ip += 2
            elif op == 4:
                a = in_arg(1)
                self.ip += 2
                return a
            elif op == 5:
                a = in_arg(1)
                b = in_arg(2)
                if a != 0:
                    self.ip = b
                else:
                    self.ip += 3
            elif op == 6:
                a = in_arg(1)
                b = in_arg(2)
                if a == 0:
                    self.ip = b
                else:
                    self.ip += 3
            elif op == 7:
                a = in_arg(1)
                b = in_arg(2)
                out_arg(3, int(a < b))
                self.ip += 4
            elif op == 8:
                a = in_arg(1)
                b = in_arg(2)
                out_arg(3, int(a == b))
                self.ip += 4
            elif op == 9:
                a = in_arg(1)
                self.rb += a
                self.ip += 2
            elif op == 99:
                return
            else:
                raise Exception("Invalid opcode {} at {}:{}".format(op, self.ip, self.program[self.ip]))


def main():
    with open('day11_input.txt') as f:
        initial_program = [int(x) for x in f.readlines()[0].split(',')]

    hull = dict()
    paint_hull(hull, Simulator(initial_program.copy()))
    print(len(hull))

    hull = dict()
    hull[0] = 1
    paint_hull(hull, Simulator(initial_program.copy()))

    minx = min(int(p.real) for p in hull)
    maxx = max(int(p.real) for p in hull)
    miny = min(int(p.imag) for p in hull)
    maxy = max(int(p.imag) for p in hull)
    out = {
        1: '⬜️',
        0: '⬛️',
    }

    for y in reversed(range(miny, maxy + 1)):
        for x in range(minx, maxx + 1):
            p = x + y * 1j
            print(out[hull.get(p, 0)], end='')
        print()


def paint_hull(hull, program):
    position = 0
    direction = 1j
    while True:
        color = 0
        if position in hull:
            color = hull[position]
        paint = program.run_to_output([color])
        if paint == 0:
            hull[position] = 0
        elif paint == 1:
            hull[position] = 1
        elif paint is None:
            break
        else:
            raise Exception('paint {}?'.format(paint))
        turn = program.run_to_output()
        if turn == 0:
            direction *= 1j
        elif turn == 1:
            direction *= -1j
        else:
            raise Exception('turn {}?'.format(turn))
        position += direction


if __name__ == "__main__":
    doctest.testmod()
    main()
