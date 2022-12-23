import doctest
from z3 import Solver, Int


def main():
    s = Solver()

    with open('day21_input.txt') as f:
        for line in f:
            name, output = line.strip().split(': ')
            if output.isnumeric():
                if name != 'humn':
                    s.add(Int(name) == int(output))
            else:
                left, op, right = output.split(' ')
                if name == 'root':
                    s.add(Int(left) == Int(right))
                else:
                    if op == '+':
                        s.add(Int(name) == Int(left) + Int(right))
                    elif op == '-':
                        s.add(Int(name) == Int(left) - Int(right))
                    elif op == '*':
                        s.add(Int(name) == Int(left) * Int(right))
                    elif op == '/':
                        s.add(Int(name) == Int(left) / Int(right))

    humn = Int('humn')
    s.check()
    m = s.model()
    print(m[humn])


if __name__ == "__main__":
    doctest.testmod()
    main()
