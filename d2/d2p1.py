import re

ranges = open('./d2/input.txt', 'r').read().split(',')

total = 0

for interval in ranges:
    split = interval.split('-')
    start = int(split[0])
    stop = int(split[1])
    print('----------------------')
    print('Start:\t', start)
    print('Stop:\t', stop)
    print()

    for x in range(start, stop+1):
        #print("Assessing:\t", x)
        length = len(str(x))
        p1 = str(x)[0:int(length/2)]
        p2 = str(x)[int(length/2):]
        if p1 == p2:
            print("Repeat found in: ", x)
            total += x

print('----------------------')
print()
print('Result: ', total)
print()
print('----------------------')