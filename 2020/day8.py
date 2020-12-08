import doctest


def run_until_loop(program):
    visited = set()
    acc = 0
    ip = 0
    while True:
        if ip in visited:
            return 'loop', acc
        elif ip >= len(program):
            return 'done', acc
        else:
            visited.add(ip)

        op, arg = program[ip]
        if op == 'acc':
            acc += arg
            ip += 1
        elif op == 'jmp':
            ip += arg
        elif op == 'nop':
            ip += 1
        else:
            raise Exception(f'unexpected instruction {ip}: {program[ip]}')


def main():
    program = []

    with open('day8_input.txt') as f:
        for line in f:
            op, arg = line.strip().split(' ')
            program.append((op, int(arg)))

    print(run_until_loop(program)[1])

    for i, (op, arg) in enumerate(program):
        if op == 'nop':
            new_program = program.copy()
            new_program[i] = ('jmp', arg)
        elif op == 'jmp':
            new_program = program.copy()
            new_program[i] = ('nop', arg)
        else:
            continue
        result, acc = run_until_loop(new_program)
        if result == 'done':
            print(acc)
            break


if __name__ == "__main__":
    doctest.testmod()
    main()
