import doctest


def sync_offset(line, size):
    for i in range(size, len(line)):
        chunk = line[i - size:i]
        if len(set(chunk)) == size:
            return i

def main():
    with open('day6_input.txt') as f:
        line = f.readline().rstrip()
        print(sync_offset(line, 4))
        print(sync_offset(line, 14))


if __name__ == "__main__":
    doctest.testmod()
    main()
