import doctest
import re


def main():
    aunts = dict()
    p = re.compile(r'(\w+): (-?\d+)')
    with open('day16_input.txt') as f:
        for line in f:
            name, stats = line.split(':', maxsplit=1)
            aunts[name] = {i: int(v) for i, v in p.findall(stats)}

    target = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1
    }

    def matches_1(info):
        for k, v in info.items():
            if target[k] != v:
                return False
        return True

    def matches_2(info):
        for k, v in info.items():
            if k == 'cats' or k == 'trees':
                if target[k] >= v:
                    return False
            elif k == 'pomeranians' or k == 'goldfish':
                if target[k] <= v:
                    return False
            elif target[k] != v:
                return False
        return True

    for name, info in aunts.items():
        if matches_1(info):
            print(name)

    for name, info in aunts.items():
        if matches_2(info):
            print(name)


if __name__ == "__main__":
    doctest.testmod()
    main()
