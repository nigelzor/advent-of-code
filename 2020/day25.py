import doctest
from itertools import count


def tsn(subject, loop):
    """
    >>> tsn(7, 8)
    5764801
    >>> tsn(7, 11)
    17807724
    """
    result = 1
    for _ in range(loop):
        result *= subject
        result %= 20201227
    return result


def reverse_tsn(subject, target):
    """
    >>> reverse_tsn(7, 5764801)
    8
    """
    result = 1
    for i in count(1):
        result *= subject
        result %= 20201227
        if result == target:
            return i


def main():
    with open('day25_input.txt') as file:
        cpk = int(file.readline().strip())
        dpk = int(file.readline().strip())

    cls = reverse_tsn(7, cpk)
    dls = reverse_tsn(7, dpk)
    cek = tsn(dpk, cls)
    dek = tsn(cpk, dls)
    print(cls, dls, cek, dek)


if __name__ == "__main__":
    doctest.testmod()
    main()
