import re

lines = open('./d1/input.txt', 'r').read().split('\n')

position = 50
solve = 0

for x in lines:
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
        solve += 1

print (solve)