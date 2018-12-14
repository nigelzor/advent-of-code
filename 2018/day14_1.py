def main(target=9):
    recipes = [3, 7]
    elves = [0, 1]

    def combine():
        total = 0
        for e, elf in enumerate(elves):
            total += recipes[elf]
        for d in [int(c) for c in str(total)]:
            recipes.append(d)
        for e, elf in enumerate(elves):
            elves[e] = (elves[e] + 1 + recipes[elf]) % len(recipes)

    while True:
        if len(recipes) >= target + 10:
            return ''.join(str(x) for x in recipes[target:(target+10)])
        combine()


if __name__ == '__main__':
    print('9:', main(9))
    print('5:', main(5))
    print('18:', main(18))
    print('2018:', main(2018))
    print('864801:', main(864801))
