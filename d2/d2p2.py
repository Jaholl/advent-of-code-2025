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
        for y in range(1, int((len(str(x)))/2)+1):
            finds = re.finditer(str(x)[0:y], str(x))
            joined_finds = ''.join([x.group() for x in finds])
            if len(joined_finds) == len(str(x)):
                print("Repeat found in: ", x, str(x)[0:y])
                total += x
                break

print('----------------------')
print()
print('Result: ', total)
print()
print('----------------------')