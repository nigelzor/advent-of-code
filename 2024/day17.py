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


def to_c(registers, instructions):
    print(f"""
int main() {{
    int a = {registers[0]};
    int b = {registers[1]};
    int c = {registers[2]};
    """)

    def combo_value(operand):
        if 0 <= operand <= 3:
            return operand
        if 4 <= operand <= 6:
            return "abc"[operand - 4]
        raise ValueError(f"invalid operand {operand}")

    for i in range(0, len(instructions), 2):
        opcode = instructions[i]
        operand = instructions[i + 1]
        print(f"label_{i}:")
        if opcode == 0:  # adv
            print(f"\ta = a / pow(2, {combo_value(operand)});")
        elif opcode == 1:  # bxl
            print(f"\tb = b ^ {operand};")
        elif opcode == 2:  # bst
            print(f"\tb = {combo_value(operand)} % 8;")
        elif opcode == 3:  # jnz
            print("    if (a != 0) {\n" f"        goto label_{operand};\n" "    }")
        elif opcode == 4:  # bxc (operand ignored)
            print("\tb = b ^ c;")
        elif opcode == 5:  # out
            print(f"\toutput({combo_value(operand)} % 8);")
        elif opcode == 6:  # bdv
            print(f"\tb = a / pow(2, {combo_value(operand)});")
        elif opcode == 7:  # cdv
            print(f"\tc = a / pow(2, {combo_value(operand)});")

    print("}")


def reconstructed(a):
    """
    >>> list(reconstructed(63281501))
    [3, 4, 3, 1, 7, 6, 5, 6, 0]
    """
    while a:
        b = a % 8
        b = b ^ 5
        c = a // pow(2, b)
        b = b ^ c
        a = a // 8
        b = b ^ 6
        yield b % 8


def part2(instructions):
    candidates = {0}
    for i in range(len(instructions)):
        to_match = instructions[-i - 1 :]
        candidates = {
            (h << 3) | t
            for h in candidates
            for t in range(8)
            if list(reconstructed((h << 3) | t)) == to_match
        }
    return min(candidates)


def main():
    with open("day17_input.txt") as f:
        lines = iter(line.strip() for line in f)
        registers = [
            int(next(lines).split(":")[1]),
            int(next(lines).split(":")[1]),
            int(next(lines).split(":")[1]),
        ]
        next(lines)
        instructions = [int(c) for c in next(lines).split(":")[1].split(",")]

    print(f"part 1: {run_for_output(registers, instructions)}")
    print(f"part 2: {part2(instructions)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
