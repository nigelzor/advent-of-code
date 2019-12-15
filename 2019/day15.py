import doctest
import itertools
import copy
import networkx as nx


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
    miny = int(min(v.imag for v in screen.keys()))
    maxy = int(max(v.imag for v in screen.keys()))
    minx = int(min(v.real for v in screen.keys()))
    maxx = int(max(v.real for v in screen.keys()))

    for y in range(miny, maxy + 1):
        y *= 1j
        for x in range(minx, maxx + 1):
            print(screen.get(x + y, '?'), end='')
        print()


DIRECTIONS = {
    1: 1j,
    4: 1,
    3: -1,
    2: -1j,
}


def main():
    with open('day15_input.txt') as f:
        initial_program = [int(x) for x in f.readlines()[0].split(',')]

    graph = nx.Graph()
    map = dict()
    pending = []
    pending.append((0, Simulator(initial_program.copy())))

    while pending:
        position, program = pending.pop()
        for i, d in DIRECTIONS.items():
            if (position + d) not in map:
                subprogram = copy.deepcopy(program)
                response = subprogram.run_to_output([i])
                if response == 0:
                    map[position + d] = '#'
                elif response == 1:
                    map[position + d] = ' '
                    graph.add_edge(position, position + d)
                    pending.append((position + d, subprogram))
                elif response == 2:
                    map[position + d] = 'O'
                    graph.add_edge(position, position + d)
                    pending.append((position + d, subprogram))
                else:
                    raise Exception('unhandled response {}'.format(response))

    display(map)

    goal = next(k for k, v in map.items() if v == 'O')
    print('steps required:', nx.shortest_path_length(graph, 0, goal))

    minute = 0
    while ' ' in map.values():
        minute += 1
        next_map = map.copy()
        for k, v in map.items():
            if v == 'O':
                for f in DIRECTIONS.values():
                    if next_map.get(k + f, None) == ' ':
                        next_map[k + f] = 'O'
        map = next_map
    print('minutes to oxygenate:', minute)


if __name__ == "__main__":
    doctest.testmod()
    main()
