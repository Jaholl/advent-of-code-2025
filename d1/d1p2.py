import re
import time
start_time = time.time()

print("Starting problem")
print("---------------------")

lines = open('./d1/input.txt', 'r').read().split('\n')

position = 50
result = 0

for x in lines:
    #print("Looking at input:", x)
    match = re.findall(r'(L|R)(\d+)', x)
    if (len(match) == 0):
        continue
    direction = match[0][0]
    steps = int(match[0][1])

    for x in range(steps):
        if (direction == "R"):
            position += 1
        else:
            position -= 1
        
        if position < 0:
            position = 99
        
        if position == 100:
            position = 0

        if (position == 0):
            result += 1
    #print("---------------------")

print("Solved problem")
print('Result:\t', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")