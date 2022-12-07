import doctest
from os import path
from collections import defaultdict

def main():
    cwd = '/'
    files = defaultdict(int)

    with open('day7_input.txt') as f:
        for line in f:
            line = line.rstrip()
            if line == '$ cd /':
                cwd = '/'
            elif line == '$ cd ..':
                cwd = path.dirname(cwd)
            elif line.startswith('$ cd '):
                cwd = path.join(cwd, line[len('$ cd '):])
            elif line == '$ ls':
                pass
            elif line.startswith('dir '):
                pass
            else:
                size = int(line.split(' ')[0])
                d = cwd
                while True:
                    files[d] += size
                    if d == '/':
                        break
                    d = path.dirname(d)

    print(sum(s for s in files.values() if s <= 100000))

    free_space = 70000000 - files['/']
    need_to_free = 30000000 - free_space
    best_candidate = None
    for k, v in files.items():
        if v >= need_to_free:
            if best_candidate is None or best_candidate > v:
                best_candidate = v
    print(best_candidate)


if __name__ == "__main__":
    doctest.testmod()
    main()
