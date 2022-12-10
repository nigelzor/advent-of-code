import doctest


class CPU:
    def __init__(self):
        self.instuctions = []
        self.cycle = 0
        self.ip = 0
        self.x = 1

    def tick(self):
        self.cycle += 1
        if self.cycle % 40 == 20:
            yield self.cycle * self.x
    def run(self):
        for instruction in self.instuctions:
            if instruction == 'noop':
                yield from self.tick()
                self.ip += 1
            elif instruction.startswith('addx '):
                val = int(instruction[5:])
                yield from self.tick()
                yield from self.tick()
                self.x += val
                self.ip += 1

def main():
    # with open('day10_sample.txt') as f:
    with open('day10_input.txt') as f:
        instructions = [line.rstrip() for line in f.readlines()]

        cpu = CPU()
        cpu.instuctions = instructions
        print(sum(s for s in cpu.run()))


if __name__ == "__main__":
    doctest.testmod()
    main()
