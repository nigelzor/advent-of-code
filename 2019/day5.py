import doctest


def simulate(program, inputs):
    """
    >>> simulate([1, 0, 0, 0, 99], None)
    [2, 0, 0, 0, 99]
    >>> simulate([2, 3, 0, 3, 99], None)
    [2, 3, 0, 6, 99]
    >>> simulate([2, 4, 4, 5, 99, 0], None)
    [2, 4, 4, 5, 99, 9801]
    >>> simulate([1, 1, 1, 4, 99, 5, 6, 0, 99], None)
    [30, 1, 1, 4, 2, 5, 6, 0, 99]
    >>> simulate([3,9,8,9,10,9,4,9,99,-1,8], [0].__iter__())
    6 : 0
    [3, 9, 8, 9, 10, 9, 4, 9, 99, 0, 8]
    >>> simulate([3,9,8,9,10,9,4,9,99,-1,8], [8].__iter__())
    6 : 1
    [3, 9, 8, 9, 10, 9, 4, 9, 99, 1, 8]
    >>> simulate([3,3,1108,-1,8,3,4,3,99], [0].__iter__())
    6 : 0
    [3, 3, 1108, 0, 8, 3, 4, 3, 99]
    >>> simulate([3,3,1108,-1,8,3,4,3,99], [8].__iter__())
    6 : 1
    [3, 3, 1108, 1, 8, 3, 4, 3, 99]
    >>> simulate([3,3,1107,-1,8,3,4,3,99], [0].__iter__())
    6 : 1
    [3, 3, 1107, 1, 8, 3, 4, 3, 99]
    >>> simulate([3,3,1107,-1,8,3,4,3,99], [8].__iter__())
    6 : 0
    [3, 3, 1107, 0, 8, 3, 4, 3, 99]
    >>> simulate([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], [0].__iter__())
    31 : 999
    [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
    >>> simulate([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], [8].__iter__())
    26 : 1000
    [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 1000, 8, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
    >>> simulate([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], [80].__iter__())
    40 : 1001
    [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 1001, 80, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
    """
    i = 0
    while True:
        op = program[i] % 100
        mode = program[i] // 100
        m_a = mode % 10
        m_b = (mode // 10) % 10
        m_c = (mode // 100) % 10

        # print('i={} op={}, f={}'.format(i, op, [m_a, m_b, m_c]))
        def param(mode, value):
            if mode == 0:
                return program[value]
            elif mode == 1:
                return value

        if op == 1:
            a = param(m_a, program[i + 1])
            b = param(m_b, program[i + 2])
            c = program[i + 3]
            program[c] = a + b
            i += 4
        elif op == 2:
            a = param(m_a, program[i + 1])
            b = param(m_b, program[i + 2])
            c = program[i + 3]
            program[c] = a * b
            i += 4
        elif op == 3:
            a = program[i + 1]
            program[a] = next(inputs)
            i += 2
        elif op == 4:
            a = param(m_a, program[i + 1])
            print(i, ':', a)
            i += 2
        elif op == 5:
            a = param(m_a, program[i + 1])
            b = param(m_b, program[i + 2])
            if a != 0:
                i = b
            else:
                i += 3
        elif op == 6:
            a = param(m_a, program[i + 1])
            b = param(m_b, program[i + 2])
            if a == 0:
                i = b
            else:
                i += 3
        elif op == 7:
            a = param(m_a, program[i + 1])
            b = param(m_b, program[i + 2])
            c = program[i + 3]
            if a < b:
                program[c] = 1
            else:
                program[c] = 0
            i += 4
        elif op == 8:
            a = param(m_a, program[i + 1])
            b = param(m_b, program[i + 2])
            c = program[i + 3]
            if a == b:
                program[c] = 1
            else:
                program[c] = 0
            i += 4
        elif op == 99:
            return program
        else:
            raise Exception("Invalid opcode {} at {}:{}".format(op, i, program[i]))


def main():
    with open('day5_input.txt') as f:
        initial_program = [int(x) for x in f.readlines()[0].split(',')]

    program = initial_program.copy()
    simulate(program, [1].__iter__())

    program = initial_program.copy()
    simulate(program, [5].__iter__())


if __name__ == "__main__":
    doctest.testmod()
    main()
