import doctest
from time import time
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
    yield from g


def fft(signal):
    output = []
    for i in range(len(signal)):
        output.append(lsd(sum(a * b for a, b in zip(signal, pattern_generator(i)))))
    return output


def main():
    # with open('day14_s.txt') as f:
    with open('day16_input.txt') as f:
        signal = [int(x) for x in f.readline().strip()]

    print(signal)
    for _ in range(100):
        signal = fft(signal)
    print(''.join(str(s) for s in signal[:8]))


if __name__ == "__main__":
    doctest.testmod()
    main()
