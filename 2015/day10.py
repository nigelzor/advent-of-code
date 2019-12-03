import doctest


def chunk(input):
    """
    >>> list(chunk("a"))
    ['a']
    >>> list(chunk("ab"))
    ['a', 'b']
    >>> list(chunk("aab"))
    ['aa', 'b']
    """
    t = None
    for c in input:
        if t is None:
            t = c
        elif t[0] == c:
            t += c
        else:
            yield t
            t = c
    if t is not None:
        yield t


def looksay(input):
    """
    >>> looksay("1")
    '11'
    >>> looksay("11")
    '21'
    >>> looksay("21")
    '1211'
    >>> looksay("1211")
    '111221'
    >>> looksay("111221")
    '312211'
    """
    return ''.join((str(len(c)) + c[0]) for c in chunk(input))


def main():
    r = '3113322113'
    for _ in range(40):
        r = looksay(r)
    print(len(r))
    for _ in range(10):
        r = looksay(r)
    print(len(r))


if __name__ == "__main__":
    doctest.testmod()
    main()
