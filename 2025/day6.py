import doctest


def product(xs):
    r = 1
    for x in xs:
        r *= x
    return r


def calculate_part1(lines):
    result = 0
    cells = [line.split() for line in lines]

    n = len(cells[1])
    for i in range(n):
        operand = cells[-1][i]
        values = [int(r[i]) for r in cells[:-1]]

        if operand == "+":
            result += sum(values)
        elif operand == "*":
            result += product(values)
    return result


def calculate_part2(lines):
    result = 0
    n = len(lines[1]) - 1  # ignore the newline

    values = []
    for c in reversed(range(n)):
        column = "".join(line[c] for line in lines)
        if not column.strip():
            values.clear()
            continue

        value = int(column[:-1])
        operand = column[-1]
        values.append(value)

        if operand == "+":
            result += sum(values)
        elif operand == "*":
            result += product(values)
    return result


def main():
    with open("day6_input.txt") as f:
        lines = f.readlines()

    part1 = calculate_part1(lines)
    print(f"Part 1: {part1}")

    part2 = calculate_part2(lines)
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
