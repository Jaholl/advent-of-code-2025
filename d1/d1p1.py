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
    if match[0][0] == "R":
        position = position + int(match[0][1])
        position = position % 100
    else:
        position = position - int(match[0][1])
        position = position % 100
    if (position == 0):
        result += 1
    #print("---------------------")

print("Solved problem")
print('Result:', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")