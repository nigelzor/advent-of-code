import doctest


def main():
    stacks = [list(x) for x in [
        'ZTFRWJG',
        'GWM',
        'JNHG',
        'JRCNW',
        'WFSBGQVM',
        'SRTDVWC',
        'HBNCDZGV',
        'SJNMGC',
        'GPNWCJDL'
    ]]

    with open('day5_input.txt') as f:
        for line in f:
            line = line.strip()
            if line.startswith('move'):
                [_, n, _, src, _, dst] = line.split(' ')
                n = int(n)
                src = int(src)
                dst = int(dst)

                # for _ in range(n):
                #     stacks[dst - 1].append(stacks[src - 1].pop())

                move = []
                for _ in range(n):
                    move.append(stacks[src - 1].pop())
                stacks[dst - 1] += reversed(move)

        print(stacks)
        print(''.join(s[len(s) - 1] for s in stacks))


if __name__ == "__main__":
    doctest.testmod()
    main()
