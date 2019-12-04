import doctest


def valid_1(s):
    if not (s[0] == s[1] or s[1] == s[2] or s[2] == s[3] or s[3] == s[4] or s[4] == s[5]):
        return False
    return True


def valid_2(s):
    if s[0] == s[1] and s[1] != s[2]:
        return True
    if s[0] != s[1] and s[1] == s[2] and s[2] != s[3]:
        return True
    if s[1] != s[2] and s[2] == s[3] and s[3] != s[4]:
        return True
    if s[2] != s[3] and s[3] == s[4] and s[4] != s[5]:
        return True
    if s[3] != s[4] and s[4] == s[5]:
        return True
    return False


def main():
    v1 = 0
    v2 = 0
    for x in range(307237, 769058 + 1):
        s = str(x)
        if s[0] > s[1] or s[1] > s[2] or s[2] > s[3] or s[3] > s[4] or s[4] > s[5]:
            continue
        if valid_1(s):
            v1 += 1
        if valid_2(s):
            v2 += 1
    print(v1)
    print(v2)


if __name__ == "__main__":
    doctest.testmod()
    main()
