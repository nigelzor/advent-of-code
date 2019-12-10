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
        self.ip = 0
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
                else:
                    raise Exception("Invalid mode {} at {}:{}".format(mode, self.ip, self.program[self.ip]))

            def out_arg(n, value):
                mode = inst[n]
                if mode != 0:
                    raise Exception("Invalid mode {} at {}:{}".format(mode, self.ip, self.program[self.ip]))
                addr = self.program[self.ip + n]
                self.program[addr] = value

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
            elif op == 99:
                return
            else:
                raise Exception("Invalid opcode {} at {}:{}".format(op, self.ip, self.program[self.ip]))


def main():
    with open('day7_input.txt') as f:
        initial_program = [int(x) for x in f.readlines()[0].split(',')]

    options = []
    for order in itertools.permutations(range(5)):
        last_out = 0
        for phase in order:
            program = Simulator(initial_program.copy())
            last_out = program.run_to_output([phase, last_out])
        options.append((last_out, order))
    print(max(options))

    options = []
    for order in itertools.permutations(range(5, 10)):
        programs = [Simulator(initial_program.copy(), [phase]) for phase in order]
        inputs = [0 for _ in order]

        while True:
            for i in range(5):
                out = programs[i].run_to_output([inputs[i]])
                if out is None:
                    break
                else:
                    inputs[(i + 1) % 5] = out
            else:
                continue
            break
        options.append((inputs[0], order))
    print(max(options))


if __name__ == "__main__":
    doctest.testmod()
    main()
