import time
start_time = time.time()

print("Starting problem")
print("---------------------")

categories = open('./d5/input.txt', 'r').read().split('\n\n')
fresh_ids = categories[0].split('\n')
ingredients = categories[1].split('\n')

fresh_dict = []
result = 0

for ingredient in ingredients:
    #print("Checking ingredient:", ingredient)
    if (ingredient == ''):
        continue
    ingredient = int(ingredient)
    for fresh_ingredient_range in fresh_ids:
        range_edges = [int(x) for x in fresh_ingredient_range.split('-')]
        if ingredient >= range_edges[0] and ingredient <= range_edges[1]:
            #print("Ingredient is fresh")
            result += 1
            break
    #print("---------------------")

print("Solved problem")
print('Result:\t', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")