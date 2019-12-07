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


def simulate(program, inputs, ip=0):
    inputs = iter(inputs)
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
            else:
                raise Exception("Invalid mode {} at {}:{}".format(mode, ip, program[ip]))

        def out_arg(n, value):
            mode = inst[n]
            if mode != 0:
                raise Exception("Invalid mode {} at {}:{}".format(mode, ip, program[ip]))
            addr = program[ip + n]
            program[addr] = value

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
            ip += 2
            return a, ip
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
        elif op == 99:
            return
        else:
            raise Exception("Invalid opcode {} at {}:{}".format(op, ip, program[ip]))


def main():
    with open('day7_input.txt') as f:
        initial_program = [int(x) for x in f.readlines()[0].split(',')]

    options = []
    for order in itertools.permutations(range(5, 10)):
        print('order', order)
        programs = [initial_program.copy() for _ in range(6)]
        a_ip = 0
        b_ip = 0
        c_ip = 0
        d_ip = 0
        e_ip = 0
        e_out = 0

        try:
            a_out, a_ip = simulate(programs[0], [order[0], e_out], a_ip)
            print('a says', a_out, a_ip)
            b_out, b_ip = simulate(programs[1], [order[1], a_out], b_ip)
            print('b says', b_out, b_ip)
            c_out, c_ip = simulate(programs[2], [order[2], b_out], c_ip)
            print('c says', c_out, c_ip)
            d_out, d_ip = simulate(programs[3], [order[3], c_out], d_ip)
            print('d says', d_out, d_ip)
            e_out, e_ip = simulate(programs[4], [order[4], d_out], e_ip)
            print('e says', e_out, e_ip)

            while True:
                a_out, a_ip = simulate(programs[0], [e_out], a_ip)
                print('a says', a_out, a_ip)
                b_out, b_ip = simulate(programs[1], [a_out], b_ip)
                print('b says', b_out, b_ip)
                c_out, c_ip = simulate(programs[2], [b_out], c_ip)
                print('c says', c_out, c_ip)
                d_out, d_ip = simulate(programs[3], [c_out], d_ip)
                print('d says', d_out, d_ip)
                e_out, e_ip = simulate(programs[4], [d_out], e_ip)
                print('e says', e_out, e_ip)
        except TypeError:
            options.append((e_out, order))

    print(max(options))


if __name__ == "__main__":
    # doctest.testmod()
    main()
