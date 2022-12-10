import doctest


class CPU:
    def __init__(self):
        self.instuctions = []
        self.screen = ['?'] * 240
        self.cycle = 0
        self.ip = 0
        self.x = 1

    def tick(self):
        x = self.cycle % 40
        lit = x-1 <= self.x <= x+1
        self.screen[self.cycle % 240] = '#' if lit else '.'
        self.cycle += 1
        return self.cycle

    def run(self):
        for instruction in self.instuctions:
            if instruction == 'noop':
                yield self.tick()
                self.ip += 1
            elif instruction.startswith('addx '):
                val = int(instruction[5:])
                yield self.tick()
                yield self.tick()
                self.x += val
                self.ip += 1

def main():
    # with open('day10_sample.txt') as f:
    with open('day10_input.txt') as f:
        instructions = [line.rstrip() for line in f.readlines()]

        cpu = CPU()
        cpu.instuctions = instructions

        part1 = 0
        for tick in cpu.run():
            if tick % 40 == 20:
                part1 += tick * cpu.x
        print(part1)

        for row in range(6):
            offset = row * 40
            print(''.join(cpu.screen[offset:offset+40]))


if __name__ == "__main__":
    doctest.testmod()
    main()
