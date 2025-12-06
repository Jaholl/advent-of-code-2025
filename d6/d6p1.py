import re

rows = open('./d6/input.txt', 'r').read().split('\n')

groups = {}
total = 0

for row in rows:
    finds = re.findall(r'\d+|\+|\*', row)
    for x in range(len(finds)):
        if x in groups.keys():
            groups[x].append(finds[x])
        else:
            groups[x] = [finds[x]]

for group in groups.values():
    if group[-1] == '*':
        sum = 1
        for x in group[:-1]:
            sum = sum * int(x)
    else:
        sum = 0
        for x in group[:-1]:
            sum += int(x)
    total += sum

print(total)