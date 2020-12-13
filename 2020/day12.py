import doctest

DIRECTIONS_1 = {
    'N': lambda p, f: (p + -1j, f),
    'S': lambda p, f: (p + 1j, f),
    'E': lambda p, f: (p + 1, f),
    'W': lambda p, f: (p + -1, f),
    'L': lambda p, f: (p, f * -1j),
    'R': lambda p, f: (p, f * 1j),
    'F': lambda p, f: (p + f, f),
}

DIRECTIONS_2 = {
    'N': lambda w, s: (w + -1j, s),
    'S': lambda w, s: (w + 1j, s),
    'E': lambda w, s: (w + 1, s),
    'W': lambda w, s: (w + -1, s),
    'L': lambda w, s: (w * -1j, s),
    'R': lambda w, s: (w * 1j, s),
    'F': lambda w, s: (w, s + w),
}


def main():
    lines = []

    with open('day12_input.txt') as file:
        for line in file:
            d = line[0]
            b = int(line[1:])
            if d in 'LR':
                b //= 90
            lines.append((d, b))

    p = 0
    f = 1
    for d, b in lines:
        for _ in range(b):
            p, f = DIRECTIONS_1[d](p, f)
        # print(p, f)
    print(abs(p.real) + abs(p.imag))

    w = 10 - 1j
    s = 0
    for d, b in lines:
        for _ in range(b):
            w, s = DIRECTIONS_2[d](w, s)
        # print(w, s)
    print(abs(s.real) + abs(s.imag))


if __name__ == "__main__":
    doctest.testmod()
    main()
