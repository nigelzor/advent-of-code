import doctest
from itertools import batched


def part1(line):
    space = []

    for id, chunk in enumerate(batched(line, 2)):
        filled = int(chunk[0])
        empty = int(chunk[1]) if len(chunk) == 2 else 0
        for _ in range(filled):
            space.append(id)
        for _ in range(empty):
            space.append(None)

    for i, c in enumerate(space):
        if c is None:
            while i < len(space):
                fill = space.pop()
                if fill is not None:
                    space[i] = fill
                    break

    return sum(i * c for i, c in enumerate(space))


def part2(line):
    files = {}
    gaps = []

    addr = 0
    for fid, chunk in enumerate(batched(line, 2)):
        filled = int(chunk[0])
        empty = int(chunk[1]) if len(chunk) == 2 else 0

        files[fid] = (addr, filled)
        addr += filled
        gaps.append((addr, empty))
        addr += empty

    for fid, (faddr, fsize) in reversed(files.items()):
        for gid, (gaddr, gsize) in enumerate(gaps):
            if gaddr > faddr:
                break
            if gsize >= fsize:
                files[fid] = (gaddr, fsize)
                gaps[gid] = (gaddr + fsize, gsize - fsize)
                break

    checksum = 0
    for fid, (faddr, fsize) in files.items():
        checksum += sum(fid * addr for addr in range(faddr, faddr + fsize))
    return checksum


def main():
    with open("day9_input.txt") as f:
        line = f.readline().strip()

    print(f"part 1: {part1(line)}")
    print(f"part 2: {part2(line)}")


if __name__ == "__main__":
    doctest.testmod()
    main()
