categories = open('./d5/input.txt', 'r').read().split('\n\n')
fresh_ids = [[int(x) for x in x.split('-')] for x in categories[0].split('\n')]

concatinations = -1
while (concatinations != 0):
    print("---------------------")
    print("FreshId length start:", len(fresh_ids))
    fresh_ids.sort()
    fresh_ingredients_intervals = []
    concatinations = 0
    for start, stop in fresh_ids:
        #print()
        #print("Running range:", start, stop)
        in_interval = False
        for interval in fresh_ingredients_intervals:
            #print("Running interval:", interval[0], interval[1])
            if start < interval[0] and interval[0] <= stop and stop <= interval[1]:
                #print(start, stop, "smaller than start", interval[0], interval[1])
                interval[0] = start
                in_interval = True
                concatinations += 1
                break
            if stop > interval[1] and interval[0] <= start and start <= interval[1]:
                #print(start, stop, "greater than end", interval[0], interval[1])
                interval[1] = stop
                in_interval = True
                concatinations += 1
                break
            if start >= interval[0] and stop <= interval[1]:
                #print(start, stop, "already in inteval", interval[0], interval[1])
                in_interval = True
                break
            if start >= interval[1] and stop <= interval[0]:
                interval[0] = start
                interval[1] = stop
                in_interval = True
                concatinations += 1
                break
        if not in_interval:
            #print("unique interval", start, stop)
            fresh_ingredients_intervals.append([start, stop])
    fresh_ids = fresh_ingredients_intervals
    print("FreshId length stop:", len(fresh_ids))
    #print(fresh_ids)

print("---------------------")
total = 0
for x in fresh_ids:
    total += x[1] - x[0] + 1
print("Total:", total)