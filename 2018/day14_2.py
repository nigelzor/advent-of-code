def main(target):
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
        return total

    while True:
        two = combine() >= 10

        if two and recipes[-(len(target) + 1):-1] == target:
            return len(recipes) - len(target) - 1
        if recipes[-len(target):] == target:
            return len(recipes) - len(target)


if __name__ == '__main__':
    print('51589:', main([int(c) for c in '51589']))
    print('01245:', main([int(c) for c in '01245']))
    print('92510:', main([int(c) for c in '92510']))
    print('59414:', main([int(c) for c in '59414']))
    print('864801:', main([int(c) for c in '864801']))
