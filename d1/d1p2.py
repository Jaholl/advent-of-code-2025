import re

lines = open('./d1/input.txt', 'r').read().split('\n')

position = 50
solve = 0

for x in lines:
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
            solve += 1

print (solve)