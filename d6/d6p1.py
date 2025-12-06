import re
import time
start_time = time.time()

print("Starting problem")
print("---------------------")

rows = open('./d6/input.txt', 'r').read().split('\n')

groups = {}
result = 0

for row in rows:
    finds = re.findall(r'\d+|\+|\*', row)
    for x in range(len(finds)):
        if x in groups.keys():
            groups[x].append(finds[x])
        else:
            groups[x] = [finds[x]]

for group in groups.values():
    #print("Evaluating group:", group)
    if group[-1] == '*':
        sum = 1
        for x in group[:-1]:
            sum = sum * int(x)
    else:
        sum = 0
        for x in group[:-1]:
            sum += int(x)
    result += sum
    #print("---------------------")

print("Solved problem")
print('Result:\t', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")