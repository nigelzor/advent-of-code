import doctest
import json


def count(o, ignore=None):
    """
    >>> count([1,2,3])
    6
    >>> count({'a':2,'b':4})
    6
    >>> count([1,'red',5], 'red')
    6
    >>> count([1,{"c":"red","b":2},3], 'red')
    4
    """
    if isinstance(o, int):
        return o
    elif isinstance(o, str):
        return 0
    elif isinstance(o, list):
        total = 0
        for v in o:
            total += count(v, ignore)
        return total
    elif isinstance(o, dict):
        if ignore and ignore in o.values():
            return 0
        total = 0
        for v in o.values():
            total += count(v, ignore)
        return total
    else:
        raise Exception("what is", o)


def main():
    with open('day12_input.txt') as f:
        books = json.load(f)

    print(count(books))
    print(count(books, 'red'))


if __name__ == "__main__":
    doctest.testmod()
    main()
