import doctest


def nice(s):
    """
    >>> nice("ugknbfddgicrmopn")
    True
    >>> nice("aaa")
    True
    >>> nice("jchzalrnumimnmhp")
    False
    >>> nice("haegwjzuvuyypxyu")
    False
    >>> nice("dvszwmarrgswjxmb")
    False
    """
    last = None
    vowels = 0
    double = False
    for c in s:
        v = "aeiou".find(c)
        if v >= 0:
            vowels += 1
        if c == last:
            double = True
        if c == 'b' and last == 'a':
            return False
        if c == 'd' and last == 'c':
            return False
        if c == 'q' and last == 'p':
            return False
        if c == 'y' and last == 'x':
            return False
        last = c
    return double and vowels > 2


def nice2(s):
    """
    >>> nice2("qjhvhtzxzqqjkmpb")
    True
    >>> nice2("xxyxx")
    True
    >>> nice2("uurcxstgmygtbstg")
    False
    >>> nice2("ieodomkazucvgmuy")
    False
    """
    has_repeat = any(s[i] == s[i + 2] for i in range(len(s) - 2))
    if not has_repeat:
        return False
    pairs = [(i, s[i-1:i+1]) for i in range(1, len(s))]
    for i, p in pairs:
        found = s.find(p, i + 1)
        if found >= 0:
            return True
    return False


def main():
    with open('day5_input.txt') as f:
        input = f.readlines()

    print(sum(1 for line in input if nice(line)))
    print(sum(1 for line in input if nice2(line)))


if __name__ == "__main__":
    doctest.testmod()
    main()
