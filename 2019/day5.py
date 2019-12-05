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


def simulate(program, inputs, debug=False):
    """
    >>> simulate([1, 0, 0, 0, 99], [], debug=True)
    [2, 0, 0, 0, 99]
    >>> simulate([2, 3, 0, 3, 99], [], debug=True)
    [2, 3, 0, 6, 99]
    >>> simulate([2, 4, 4, 5, 99, 0], [], debug=True)
    [2, 4, 4, 5, 99, 9801]
    >>> simulate([1, 1, 1, 4, 99, 5, 6, 0, 99], [], debug=True)
    [30, 1, 1, 4, 2, 5, 6, 0, 99]
    >>> simulate([3,9,8,9,10,9,4,9,99,-1,8], [0], debug=True)
    6 : 0
    [3, 9, 8, 9, 10, 9, 4, 9, 99, 0, 8]
    >>> simulate([3,9,8,9,10,9,4,9,99,-1,8], [8], debug=True)
    6 : 1
    [3, 9, 8, 9, 10, 9, 4, 9, 99, 1, 8]
    >>> simulate([3,3,1108,-1,8,3,4,3,99], [0], debug=True)
    6 : 0
    [3, 3, 1108, 0, 8, 3, 4, 3, 99]
    >>> simulate([3,3,1108,-1,8,3,4,3,99], [8], debug=True)
    6 : 1
    [3, 3, 1108, 1, 8, 3, 4, 3, 99]
    >>> simulate([3,3,1107,-1,8,3,4,3,99], [0], debug=True)
    6 : 1
    [3, 3, 1107, 1, 8, 3, 4, 3, 99]
    >>> simulate([3,3,1107,-1,8,3,4,3,99], [8], debug=True)
    6 : 0
    [3, 3, 1107, 0, 8, 3, 4, 3, 99]
    >>> simulate([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], [0])
    31 : 999
    46 : done
    >>> simulate([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], [8])
    26 : 1000
    46 : done
    >>> simulate([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], [80])
    40 : 1001
    46 : done
    """
    inputs = iter(inputs)
    ip = 0
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
            print(ip, ':', a)
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
        elif op == 99:
            if debug:
                return program
            print(ip, ':', 'done')
            return
        else:
            raise Exception("Invalid opcode {} at {}:{}".format(op, ip, program[ip]))


def main():
    with open('day5_input.txt') as f:
        initial_program = [int(x) for x in f.readlines()[0].split(',')]

    program = initial_program.copy()
    simulate(program, [1])

    program = initial_program.copy()
    simulate(program, [5])


if __name__ == "__main__":
    doctest.testmod()
    main()
