import time
start_time = time.time()

print("Starting problem")
print("---------------------")

categories = open('./d5/input.txt', 'r').read().split('\n\n')
fresh_ids = [[int(x) for x in x.split('-')] for x in categories[0].split('\n')]

concatinations = -1
while (concatinations != 0):
    #print("FreshId length start:", len(fresh_ids))
    fresh_ids.sort()
    fresh_ingredients_intervals = []
    concatinations = 0
    for start, stop in fresh_ids:
        #print("Running range:", start, stop)
        in_interval = False
        for interval in fresh_ingredients_intervals:
            #print("Running interval:", interval[0], interval[1])
            if start < interval[0] and interval[0] <= stop and stop <= interval[1]:
                interval[0] = start
                in_interval = True
                concatinations += 1
                break
            if stop > interval[1] and interval[0] <= start and start <= interval[1]:
                interval[1] = stop
                in_interval = True
                concatinations += 1
                break
            if start >= interval[0] and stop <= interval[1]:
                in_interval = True
                break
            if start >= interval[1] and stop <= interval[0]:
                interval[0] = start
                interval[1] = stop
                in_interval = True
                concatinations += 1
                break
        if not in_interval:
            fresh_ingredients_intervals.append([start, stop])
    fresh_ids = fresh_ingredients_intervals
    #print("FreshId length stop:", len(fresh_ids))

    #print("---------------------")
result = 0
for x in fresh_ids:
    result += x[1] - x[0] + 1

print("Solved problem")
print('Result:\t', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")