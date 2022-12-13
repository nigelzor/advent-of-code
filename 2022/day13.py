import doctest


def main():
    i = 0
    ok = 0
    a = None
    b = None

    def process(left, right):
        nonlocal i, ok
        i += 1
        print('compare', left, right)
        result = compare(left, right)
        if result is not False:
            ok += i
            print(i, result, ok)

    def compare(left, right):
        print('  compare', left, right)
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
                    print('right is smaller')
                    return False
            else:
                if len(right) < len(left):
                    print('right ran out')
                    return False
                if len(left) < len(right):
                    print('left ran out')
                    return True


    with open('day13_input.txt') as f:
        for line in f:
            line = line.strip()

            if not line:
                a = None
                b = None
            elif a is not None:
                b = eval(line)
                process(a, b)
            else:
                a = eval(line)

    print(ok)

if __name__ == "__main__":
    doctest.testmod()
    main()
