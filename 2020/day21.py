import doctest
from collections import defaultdict
import re


def main():
    recipes = []
    with open('day21_input.txt') as file:
        for line in file:
            m = re.fullmatch(r'(.*) \(contains (.*)\)', line.strip())
            ingredients, allergens = m.groups()
            ingredients = ingredients.split(' ')
            allergens = allergens.split(', ')
            recipes.append((ingredients, allergens))

    all_allergens = set()
    all_ingredients = set()
    for ingredients, allergens in recipes:
        for i in ingredients:
            all_ingredients.add(i)
        for a in allergens:
            all_allergens.add(a)

    allergen_ingredients = defaultdict(lambda: set(all_ingredients))
    for ingredients, allergens in recipes:
        for a in allergens:
            allergen_ingredients[a] &= set(ingredients)
            # print(a, 'could be', allergen_ingredients[a])

    safe_ingredients = set(all_ingredients)
    for ingredients in allergen_ingredients.values():
        safe_ingredients -= ingredients
    # print(f'safe: {safe_ingredients}')

    part1_count = 0
    for ingredients, allergens in recipes:
        part1_count += len(set(ingredients) & safe_ingredients)

    print(part1_count)

    while any(len(v) > 1 for v in allergen_ingredients.values()):
        for a1, i1 in allergen_ingredients.items():
            if len(i1) == 1:
                for a2, i2 in allergen_ingredients.items():
                    if a1 != a2:
                        i2 -= i1

    dangerous = [(a, next(iter(i))) for a, i in allergen_ingredients.items()]
    dangerous.sort()
    print(','.join(x[1] for x in dangerous))


if __name__ == "__main__":
    doctest.testmod()
    main()
