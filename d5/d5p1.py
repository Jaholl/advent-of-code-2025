import re

categories = open('./d5/input.txt', 'r').read().split('\n\n')
fresh_ids = categories[0].split('\n')
ingredients = categories[1].split('\n')

fresh_dict = []
fresh_ingredients_total = 0

for ingredient in ingredients:
    if (ingredient == ''):
        continue
    ingredient = int(ingredient)
    for fresh_ingredient_range in fresh_ids:
        range_edges = [int(x) for x in fresh_ingredient_range.split('-')]
        if ingredient >= range_edges[0] and ingredient <= range_edges[1]:
            print(ingredient)
            fresh_ingredients_total += 1
            break

print(fresh_ingredients_total)