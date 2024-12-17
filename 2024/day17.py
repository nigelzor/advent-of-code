import doctest


class Computer:
    def __init__(self):
        self.registers = [0, 0, 0]
        self.instructions = []
        self.ip = 0
        self.output = []

    def combo_value(self, operand):
        if 0 <= operand <= 3:
            return operand
        if 4 <= operand <= 6:
            return self.registers[operand - 4]
        raise ValueError(f"invalid operand {operand}")

    def next(self):
        try:
            opcode = self.instructions[self.ip]
            operand = self.instructions[self.ip + 1]
        except IndexError:
            return False

        next_ip = self.ip + 2

        if opcode == 0:  # adv
            self.registers[0] = self.registers[0] // (2 ** self.combo_value(operand))
        elif opcode == 1:  # bxl
            self.registers[1] = self.registers[1] ^ operand
        elif opcode == 2:  # bst
            self.registers[1] = self.combo_value(operand) % 8
        elif opcode == 3:  # jnz
            if self.registers[0] != 0:
                next_ip = operand
        elif opcode == 4:  # bxc (operand ignored)
            self.registers[1] = self.registers[1] ^ self.registers[2]
        elif opcode == 5:  # out
            self.output.append(self.combo_value(operand) % 8)
        elif opcode == 6:  # bdv
            self.registers[1] = self.registers[0] // (2 ** self.combo_value(operand))
        elif opcode == 7:  # cdv
            self.registers[2] = self.registers[0] // (2 ** self.combo_value(operand))
        self.ip = next_ip

        return True


def run_to_completion(registers, instructions):
    """
    >>> run_to_completion([0,0,9], [2,6]).registers[1]
    1
    >>> run_to_completion([2024,0,0], [0,1,5,4,3,0]).registers[0]
    0
    >>> run_to_completion([0,29,0], [1,7]).registers[1]
    26
    >>> run_to_completion([0,2024,43690], [4,0]).registers[1]
    44354
    """
    computer = Computer()
    computer.registers = registers[:]
    computer.instructions = instructions[:]
    while computer.next():
        pass
    return computer


def run_for_output(registers, instructions):
    """
    >>> run_for_output([10,0,0], [5,0,5,1,5,4])
    '0,1,2'
    >>> run_for_output([2024,0,0], [0,1,5,4,3,0])
    '4,2,5,6,7,7,7,7,3,1,0'
    >>> run_for_output([729,0,0], [0,1,5,4,3,0])
    '4,6,3,5,6,3,5,2,1,0'
    """
    computer = run_to_completion(registers, instructions)
    return ",".join((str(c) for c in computer.output))


def main():
    registers = []

    with open("day17_input.txt") as f:
        lines = iter(line.strip() for line in f)

        registers.append(int(next(lines).split(":")[1]))
        registers.append(int(next(lines).split(":")[1]))
        registers.append(int(next(lines).split(":")[1]))
        next(lines)
        instructions = [int(c) for c in next(lines).split(":")[1].split(",")]

    print(f"part 1: {run_for_output(registers, instructions)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
