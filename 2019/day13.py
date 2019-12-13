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


def display(screen):
    out = {
        None: ' ',
        0: ' ',
        1: 'W',
        2: 'B',
        3: '_',
        4: '*',
    }
    height = max(y for x, y in screen.keys())
    width = max(x for x, y in screen.keys())

    print('score:', screen[(-1, 0)])
    for y in range(0, height + 1):
        for x in range(0, width + 1):
            print(out[screen.get((x, y), None)], end='')
        print()



def main():
    with open('day13_input.txt') as f:
        initial_program = [int(x) for x in f.readlines()[0].split(',')]

    program = Simulator(initial_program.copy())
    output = program.run_to_completion()
    nblocks = 0
    for i in range(0, len(output), 3):
        t = output[i + 2]
        if t == 2:
            nblocks += 1
    print(nblocks)

    ball_x = 0
    paddle_x = 0

    def generate_input():
        while True:
            if ball_x < paddle_x:
                yield -1
            elif ball_x > paddle_x:
                yield 1
            else:
                yield 0

    program = Simulator(initial_program.copy(), generate_input())
    program.program[0] = 2
    screen = dict()
    while True:
        x = program.run_to_output()
        if x is None:
            break
        y = program.run_to_output()
        t = program.run_to_output()
        if t == 4:
            ball_x = x
        if t == 3:
            paddle_x = x
        screen[x, y] = t

    display(screen)


if __name__ == "__main__":
    doctest.testmod()
    main()
