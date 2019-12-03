import doctest
from hashlib import md5


def mine_md5(key, prefix):
    """
    >>> mine_md5("abcdef", "00000")
    609043
    """
    for n in range(0, 1000000000):
        hash = md5((key + str(n)).encode()).hexdigest()
        if hash.startswith(prefix):
            return n


def main():
    print(mine_md5("yzbqklnj", "00000"))
    print(mine_md5("yzbqklnj", "000000"))


if __name__ == "__main__":
    doctest.testmod()
    main()
