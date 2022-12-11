import doctest

class Monkey:
    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.total_inspections = 0

    def turn(self, monkeys):
        to_inspect = self.items
        self.items = []
        for item in to_inspect:
            self.total_inspections += 1

            print(f"Monkey inspects an item with a worry level of {item}.")
            worry = eval(self.operation.replace('old', str(item))) // 3
            is_divisible = worry % self.test == 0
            print(f"Current worry level is {is_divisible} divisible by {self.test}.")
            target = self.if_true if is_divisible else self.if_false
            print(f"Item with worry level of {worry} is thrown to {target}.")
            monkeys[target].items.append(worry)


def main():
    monkeys = []

    # with open('day11_sample.txt') as f:
    with open('day11_input.txt') as f:
        for line in f:
            line = line.strip()

            if line.startswith('Starting items: '):
                items = line[len('Starting items: '):].split(', ')
            elif line.startswith('Operation: '):
                operation = line.split('=')[1]
            elif line.startswith('Test: '):
                test = int(line.split(' ')[-1])
            elif line.startswith('If true: '):
                if_true = int(line.split(' ')[-1])
            elif line.startswith('If false: '):
                if_false = int(line.split(' ')[-1])
            elif line == '':
                monkeys.append(Monkey(items, operation, test, if_true, if_false))
        else:
            monkeys.append(Monkey(items, operation, test, if_true, if_false))

    for round in range(20):
        for i, monkey in enumerate(monkeys):
            monkey.turn(monkeys)

    for i, monkey in enumerate(monkeys):
        print(f"Monkey {i} inspected items {monkey.total_inspections} times.")

    most_active = sorted([m.total_inspections for m in monkeys])[-2:]
    monkey_business = 1
    for a in most_active:
        monkey_business *= a
    print(monkey_business)


if __name__ == "__main__":
    doctest.testmod()
    main()
