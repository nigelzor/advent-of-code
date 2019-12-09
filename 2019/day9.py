import doctest


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


def simulate(program, inputs, ip=0, rb=0):
    inputs = iter(inputs)
    outputs = []
    while True:
        inst = decode(program[ip])
        op = inst[0]

        # print('ip={} inst={}'.format(ip, inst))
        def in_arg(n):
            value = program[ip + n]
            mode = inst[n]
            if mode == 0:
                return program[value]
            elif mode == 1:
                return value
            elif mode == 2:
                return program[value + rb]
            else:
                raise Exception("Invalid mode {} at {}:{}".format(mode, ip, program[ip]))

        def out_arg(n, value):
            mode = inst[n]
            addr = program[ip + n]
            if mode == 0:
                program[addr] = value
            elif mode == 2:
                program[addr + rb] = value
            else:
                raise Exception("Invalid mode {} at {}:{}".format(mode, ip, program[ip]))

        if op == 1:
            a = in_arg(1)
            b = in_arg(2)
            out_arg(3, a + b)
            ip += 4
        elif op == 2:
            a = in_arg(1)
            b = in_arg(2)
            out_arg(3, a * b)
            ip += 4
        elif op == 3:
            out_arg(1, next(inputs))
            ip += 2
        elif op == 4:
            a = in_arg(1)
            outputs.append(a)
            ip += 2
        elif op == 5:
            a = in_arg(1)
            b = in_arg(2)
            if a != 0:
                ip = b
            else:
                ip += 3
        elif op == 6:
            a = in_arg(1)
            b = in_arg(2)
            if a == 0:
                ip = b
            else:
                ip += 3
        elif op == 7:
            a = in_arg(1)
            b = in_arg(2)
            out_arg(3, int(a < b))
            ip += 4
        elif op == 8:
            a = in_arg(1)
            b = in_arg(2)
            out_arg(3, int(a == b))
            ip += 4
        elif op == 9:
            a = in_arg(1)
            rb += a
            ip += 2
        elif op == 99:
            return outputs
        else:
            raise Exception("Invalid opcode {} at {}:{}".format(op, ip, program[ip]))


def main():
    with open('day9_input.txt') as f:
        initial_program = [int(x) for x in f.readlines()[0].split(',')]
        initial_program.extend(0 for _ in range(1000))

    test_program = initial_program.copy()
    out = simulate(test_program, [1])
    print(out)

    boost_program = initial_program.copy()
    out = simulate(boost_program, [2])
    print(out)


if __name__ == "__main__":
    doctest.testmod()
    main()
