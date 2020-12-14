import doctest


def part1(lines):
    mask = lambda x: x
    mem = dict()
    for addr, val in lines:
        if addr == 'mask':
            mask1 = int(val.replace('X', '0'), 2)
            mask2 = int(val.replace('X', '1'), 2)
            mask = lambda x: (x | mask1) & mask2
        else:
            mem[addr] = mask(val)
    print(sum(mem.values()))


def all_addrs(addr, mask, at=0):
    """
    >>> list(all_addrs('1', '1'))
    ['1']
    >>> list(all_addrs('0', '1'))
    ['1']
    >>> list(all_addrs('0', 'X'))
    ['0', '1']
    """
    if at == len(mask):
        yield ''
    elif mask[at] == '0':
        for rest in all_addrs(addr, mask, at + 1):
            yield addr[at] + rest
    elif mask[at] == '1':
        for rest in all_addrs(addr, mask, at + 1):
            yield '1' + rest
    else:
        for rest in all_addrs(addr, mask, at + 1):
            yield '0' + rest
            yield '1' + rest


def part2(lines):
    mask = None
    mem = dict()
    for addr, val in lines:
        if addr == 'mask':
            mask = val
        else:
            addr = bin(addr)[2:].zfill(36)
            for a in all_addrs(addr, mask):
                mem[a] = val
    print(sum(mem.values()))


def main():
    lines = []
    with open('day14_input.txt') as file:
        for line in file:
            addr, val = line.strip().split(' = ')
            if addr == 'mask':
                lines.append((addr, val))
            else:
                lines.append((int(addr[4:-1]), int(val)))

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    doctest.testmod()
    main()
