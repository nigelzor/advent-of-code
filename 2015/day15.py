import doctest
import re
from collections import defaultdict


def score_1(ingredients, recipe):
    """
    >>> score_1({'Butterscotch':{'capacity':-1,'durability':-2,'flavor':6,'texture':3,'calories':8},'Cinnamon':{'capacity':2,'durability':3,'flavor':-2,'texture':-1,'calories':3}}, {'Butterscotch':44,'Cinnamon':56})
    62842880
    """
    total_amount = sum(recipe.values())
    if total_amount != 100:
        raise Exception('total_amount = {}'.format(total_amount))
    attrs = defaultdict(int)
    for name, amt in recipe.items():
        for attr, value in ingredients[name].items():
            attrs[attr] += amt * value
    total = 1
    for n, v in attrs.items():
        if n != 'calories':
            total *= max(v, 0)
    return total


def score_2(ingredients, recipe):
    calories = sum(ingredients[n]['calories'] * amt for n, amt in recipe.items())
    if calories != 500:
        return -1
    return score_1(ingredients, recipe)


def optimal(ingredients, partial_recipe, score):
    remaining = 100 - sum(partial_recipe.values())
    if remaining < 0:
        raise Exception('remaining = {}'.format(remaining))
    elif remaining == 0:
        return score(ingredients, partial_recipe), partial_recipe
    else:
        def new_recipe(ingredient, amt):
            r = dict(partial_recipe)
            r[ingredient] = amt
            return r

        to_add = ingredients.keys() - partial_recipe.keys()
        adding = min(to_add)
        if len(to_add) == 1:
            r = new_recipe(adding, remaining)
            return score(ingredients, r), r
        else:
            return max((optimal(ingredients, new_recipe(adding, i), score) for i in range(0, remaining + 1)), key=lambda x: x[0])


def main():
    ingredients = dict()
    p = re.compile(r'(\w+) (-?\d+)')
    with open('day15_input.txt') as f:
        for line in f:
            name, stats = line.split(':', maxsplit=1)
            ingredients[name] = {i: int(v) for i, v in p.findall(stats)}

    print(optimal(ingredients, dict(), score_1))
    print(optimal(ingredients, dict(), score_2))


if __name__ == "__main__":
    doctest.testmod()
    main()
