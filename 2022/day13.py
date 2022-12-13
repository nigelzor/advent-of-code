import doctest
from functools import cmp_to_key


def main():
    i = 0
    ok = 0
    a = None
    b = None

    def process(left, right):
        nonlocal i, ok
        i += 1
        # print('compare', left, right)
        result = compare(left, right)
        if result is not False:
            ok += i

    def compare(left, right):
        # print('  compare', left, right)
        if isinstance(left, int) != isinstance(right, int):
            if isinstance(left, int):
                return compare([left], right)
            else:
                return compare(left, [right])

        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return True
            if left > right:
                return False
        elif isinstance(left, list) and isinstance(right, list):
            for l, r in zip(left, right):
                c = compare(l, r)
                if c is True:
                    return True
                if c is False:
                    # print('right is smaller')
                    return False
            else:
                if len(right) < len(left):
                    # print('right ran out')
                    return False
                if len(left) < len(right):
                    # print('left ran out')
                    return True

    packets = []

    with open("day13_input.txt") as f:
        for line in f:
            line = line.strip()

            if not line:
                a = None
                b = None
            elif a is not None:
                b = eval(line)
                packets.append(b)
                process(a, b)
            else:
                a = eval(line)
                packets.append(a)

    print(ok)

    def comparator(left, right):
        if compare(left, right) is False:
            return -1
        return 0

    packets.append([[2]])
    packets.append([[6]])
    packets.sort(key=cmp_to_key(comparator))
    packets.reverse()

    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))


if __name__ == "__main__":
    doctest.testmod()
    main()
