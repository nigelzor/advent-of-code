import doctest


def simulate(program):
    """
    >>> simulate([1, 0, 0, 0, 99])
    [2, 0, 0, 0, 99]
    >>> simulate([2, 3, 0, 3, 99])
    [2, 3, 0, 6, 99]
    >>> simulate([2, 4, 4, 5, 99, 0])
    [2, 4, 4, 5, 99, 9801]
    >>> simulate([1, 1, 1, 4, 99, 5, 6, 0, 99])
    [30, 1, 1, 4, 2, 5, 6, 0, 99]
    """
    i = 0
    while True:
        op = program[i]
        if op == 1:
            a = program[i + 1]
            b = program[i + 2]
            c = program[i + 3]
            program[c] = program[a] + program[b]
            i += 4
        elif op == 2:
            a = program[i + 1]
            b = program[i + 2]
            c = program[i + 3]
            program[c] = program[a] * program[b]
            i += 4
        elif op == 99:
            return program
        else:
            raise Exception("Invalid opcode")


def main():
    with open('day2_input.txt') as f:
        initial_program = [int(x) for x in f.readlines()[0].split(',')]

    program = initial_program.copy()
    program[1] = 12
    program[2] = 2
    done = simulate(program)
    print(done[0])

    for noun in range(0, 100):
        for verb in range(0, 100):
            program = initial_program.copy()
            program[1] = noun
            program[2] = verb
            try:
                done = simulate(program)
                if done[0] == 19690720:
                    print(100 * noun + verb)
            except:
                pass


if __name__ == "__main__":
    doctest.testmod()
    main()
