import doctest
from copy import deepcopy


def product(xs):
    p = 1
    for x in xs:
        p *= x
    return p


class Monkey:
    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.total_inspections = 0

    def turn(self, monkeys, manage):
        to_inspect = self.items
        self.items = []

        for item in to_inspect:
            self.total_inspections += 1

            # print(f"Monkey inspects an item with a worry level of {item}.")
            worry = self.operation(item)
            worry = manage(worry)
            # print(f"Worry level is ? to {worry}.")
            is_divisible = worry % self.test == 0
            # print(f"Current worry level is {is_divisible} divisible by {self.test}.")
            target = self.if_true if is_divisible else self.if_false
            # print(f"Item with worry level of {worry} is thrown to {target}.")
            monkeys[target].items.append(worry)


def part1(monkeys):
    for round in range(20):
        for i, monkey in enumerate(monkeys):
            monkey.turn(monkeys, lambda x: x // 3)

    most_active = sorted(m.total_inspections for m in monkeys)[-2:]
    print(product(most_active))


def part2(monkeys, modulo):
    for round in range(10000):
        for i, monkey in enumerate(monkeys):
            monkey.turn(monkeys, lambda x: x % modulo)

    # if round == 0 or round == 19 or round % 1000 == 999:
    #     print(f"After round {round + 1}")
    #     for i, monkey in enumerate(monkeys):
    #         print(f"Monkey {i} inspected items {monkey.total_inspections} times.")
    #         print(f"Monkey {i}: {', '.join(str(i) for i in monkey.items)}")

    most_active = sorted(m.total_inspections for m in monkeys)[-2:]
    print(product(most_active))


def main():
    modulo = 1
    monkeys = []

    def parse_operation(operation):
        nonlocal modulo
        if operation == 'old * old':
            return lambda x: x * x
        elif operation.startswith('old * '):
            factor = int(operation.split(' ')[-1])
            modulo *= factor
            return lambda x: x * factor
        elif operation.startswith('old + '):
            factor = int(operation.split(' ')[-1])
            modulo *= factor
            return lambda x: x + factor
        else:
            raise Exception('what to do with ' + operation)

    # with open('day11_sample.txt') as f:
    with open('day11_input.txt') as f:
        for line in f:
            line = line.strip()

            if line.startswith('Starting items: '):
                items = [int(i) for i in line[len('Starting items: '):].split(', ')]
            elif line.startswith('Operation: '):
                operation = parse_operation(line.split('= ')[1])
            elif line.startswith('Test: '):
                test = int(line.split(' ')[-1])
                modulo *= test
            elif line.startswith('If true: '):
                if_true = int(line.split(' ')[-1])
            elif line.startswith('If false: '):
                if_false = int(line.split(' ')[-1])
            elif line == '':
                monkeys.append(Monkey(items, operation, test, if_true, if_false))
        else:
            monkeys.append(Monkey(items, operation, test, if_true, if_false))

    part1(deepcopy(monkeys))
    part2(deepcopy(monkeys), modulo)


if __name__ == "__main__":
    doctest.testmod()
    main()
