with open('day8.txt') as f:
    numbers = [int(x) for x in f.readline().split(' ')]

    # print(numbers)
    numbers.reverse()

    def read(numbers):
        total_m = 0
        n_c = numbers.pop()
        n_m = numbers.pop()
        # print('read', n_c, n_m)
        child_total = [read(numbers) for _ in range(n_c)]
        for i in range(n_m):
            m = numbers.pop()
            if n_c == 0:
                total_m += m
            elif m and m <= len(child_total):
                total_m += child_total[m - 1]
        # print('total', total_m)
        return total_m

    total_m = read(numbers)
    print('metadata total:', total_m)
