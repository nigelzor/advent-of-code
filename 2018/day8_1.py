with open('day8.txt') as f:
    numbers = [int(x) for x in f.readline().split(' ')]

    # print(numbers)
    numbers.reverse()

    def read(numbers):
        total_m = 0
        n_c = numbers.pop()
        n_m = numbers.pop()
        # print('read', n_c, n_m)
        for i in range(n_c):
            total_m += read(numbers)
        for i in range(n_m):
            total_m += numbers.pop()
        return total_m

    total_m = read(numbers)
    print('metadata total:', total_m)
