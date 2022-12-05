import doctest


def insert(lists, c, v):
    while len(lists) <= c:
        lists.append([])
    lists[c].insert(0, v)


def main():
    stacks1 = []
    stacks2 = []
    with open('day5_input.txt') as f:
        for line in f:
            if '[' in line:
                for i, c in enumerate(line):
                    if 'A' <= c <= 'Z':
                        col = i // 4
                        insert(stacks1, col, c)
                        insert(stacks2, col, c)

            elif line.startswith('move'):
                [_, n, _, src, _, dst] = line.split(' ')
                n = int(n)
                src = int(src)
                dst = int(dst)

                for _ in range(n):
                    stacks1[dst - 1].append(stacks1[src - 1].pop())

                move = []
                for _ in range(n):
                    move.append(stacks2[src - 1].pop())
                stacks2[dst - 1] += reversed(move)

        print(''.join(s[len(s) - 1] for s in stacks1))
        print(''.join(s[len(s) - 1] for s in stacks2))


if __name__ == "__main__":
    doctest.testmod()
    main()
