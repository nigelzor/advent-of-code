import doctest


def possible(target, current, numbers):
    if not numbers:
        return target == current
    return possible(target, current + numbers[0], numbers[1:]) or possible(
        target, current * numbers[0], numbers[1:]
    )


def possible_2(target, current, numbers):
    if not numbers:
        return target == current
    return (
        possible_2(target, current + numbers[0], numbers[1:])
        or possible_2(target, current * numbers[0], numbers[1:])
        or possible_2(target, int(str(current) + str(numbers[0])), numbers[1:])
    )


def main():
    part1 = 0
    part2 = 0

    with open("day7_input.txt") as f:
        for line in f:
            result, numbers = line.split(": ")
            result = int(result)
            numbers = [int(n) for n in numbers.split()]
            if possible(result, numbers[0], numbers[1:]):
                part1 += result
                part2 += result
            elif possible_2(result, numbers[0], numbers[1:]):
                part2 += result

    print(f"part 1: {part1}")
    print(f"part 2: {part2}")


if __name__ == "__main__":
    doctest.testmod()
    main()
