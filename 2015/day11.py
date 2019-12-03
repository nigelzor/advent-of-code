import doctest

from collections import defaultdict


def inc(input):
    """
    >>> inc('a')
    'b'
    >>> inc('az')
    'ba'
    """
    p = len(input)
    while p > 0:
        p -= 1
        if input[p] < 'z':
            c = chr(ord(input[p]) + 1)
            return input[:p] + c + input[p+1:]
        else:
            input = input[:p] + 'a' + input[p+1:]


def has_triplet(input):
    """
    >>> has_triplet("a")
    False
    >>> has_triplet("abc")
    True
    >>> has_triplet("abd")
    False
    """
    for i in range(len(input) - 2):
        if ord(input[i + 2]) == ord(input[i + 1]) + 1 and ord(input[i + 1]) == ord(input[i]) + 1:
            return True
    return False


def has_pairs(input):
    pairs = defaultdict(int)
    last = None
    for c in input:
        if last == c:
            pair = c + c
            pairs[pair] += 1
            if len(pairs) > 1:
                return True
        last = c
    return False


def valid(input):
    """
    >>> valid("hijklmmn")
    False
    >>> valid("abbceffg")
    False
    >>> valid("abbcegjk")
    False
    """
    for c in input:
        if c == 'i' or c == 'o' or c == 'l':
            return False
    if not has_triplet(input):
        return False
    if not has_pairs(input):
        return False
    return True


def next_password(input):
    """
    >>> next_password("abcdefgh")
    'abcdffaa'
    >>> next_password("ghijklmn")
    'ghjaabcc'
    """
    while True:
        input = inc(input)
        if valid(input):
            return input


def main():
    a = next_password("vzbxkghb")
    print(a)
    b = next_password(a)
    print(b)


if __name__ == "__main__":
    doctest.testmod()
    main()
