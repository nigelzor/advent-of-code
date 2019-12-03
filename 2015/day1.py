import doctest


def main():
    with open('day1_input.txt') as f:
        instructions = f.readlines()[0]

    up = sum(1 for c in instructions if c == '(')
    down = sum(1 for c in instructions if c == ')')
    print(up - down)

    p = 0
    for i, c in enumerate(instructions):
        if c == '(':
            p += 1
        elif c == ')':
            p -= 1
            if p < 0:
                print(i + 1)
                break


if __name__ == "__main__":
    doctest.testmod()
    main()
