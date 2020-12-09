import doctest
from collections import deque


def valid(numbers, n):
    for a in numbers:
        for b in numbers:
            if a != b and a + b == n:
                return True
    return False


def part1(lines):
    window = deque()

    for n in lines:
        if len(window) < 25:
            window.append(n)
        else:
            if valid(window, n):
                window.append(n)
                window.popleft()
            else:
                return n


def part2(lines, target):
    for a in range(len(lines)):
        t = lines[a]
        for b in range(a + 1, len(lines)):
            t += lines[b]
            if t == target:
                lo = min(lines[a:b + 1])
                hi = max(lines[a:b + 1])
                return lo + hi
            elif t > target:
                break


def main():
    lines = []
    with open('day9_input.txt') as f:
        for line in f:
            lines.append(int(line))

    invalid = part1(lines)
    print(invalid)
    print(part2(lines, invalid))


if __name__ == "__main__":
    doctest.testmod()
    main()
