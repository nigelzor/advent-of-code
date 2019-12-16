import doctest
from itertools import islice


def lsd(n):
    """
    >>> lsd(38)
    8
    >>> lsd(-17)
    7
    """
    return abs(n) % 10


def pattern_generator_0(n):
    while True:
        for v in [0, 1, 0, -1]:
            for _ in range(n + 1):
                yield v


def pattern_generator(n):
    """
    >>> list(islice(pattern_generator(1), 15))
    [0, 1, 1, 0, 0, -1, -1, 0, 0, 1, 1, 0, 0, -1, -1]
    """
    g = pattern_generator_0(n)
    next(g)
    return g


def fft(signal):
    output = []
    for i in range(len(signal)):
        output.append(lsd(sum(a * b for a, b in zip(signal, pattern_generator(i)))))
    return output


def fake_fft_tail(signal):
    total = 0
    output = []
    for v in reversed(signal):
        total = lsd(total + v)
        output.append(total)
    output.reverse()
    return output


def part1(signal):
    for _ in range(100):
        signal = fft(signal)
    print('1:', ''.join(str(s) for s in signal[:8]))


def part2(signal):
    signal = signal * 10000
    offset = int(''.join(str(s) for s in signal[:7]))

    for n in range(100):
        signal = fake_fft_tail(signal)
    print('2:', ''.join(str(s) for s in signal[offset:offset+8]))


def main():
    with open('day16_input.txt') as f:
        signal = [int(x) for x in f.readline().strip()]
        # signal = [int(x) for x in '03036732577212944063491565474664']

    part1(signal)
    part2(signal)


if __name__ == "__main__":
    doctest.testmod()
    main()
