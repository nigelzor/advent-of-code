import doctest


def main():
    results = dict()
    pending = dict()

    with open('day21_input.txt') as f:
        for line in f:
            name, output = line.strip().split(': ')
            if output.isnumeric():
                results[name] = int(output)
            else:
                left, op, right = output.split(' ')
                pending[name] = (left, op, right)

    while pending:
        for name, (left, op, right) in pending.items():
            if left in results and right in results:
                results[name] = eval(f'{results[left]} {op} {results[right]}')
                del pending[name]
                break

    print(results['root'])


if __name__ == "__main__":
    doctest.testmod()
    main()
