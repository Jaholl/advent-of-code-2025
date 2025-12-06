import re
import time
start_time = time.time()

print("Starting problem")
print("---------------------")

ranges = open('./d2/input.txt', 'r').read().split(',')

result = 0

for interval in ranges:
    split = interval.split('-')
    start = int(split[0])
    stop = int(split[1])
    #print('Start:\t', start)
    #print('Stop:\t', stop)
    #print()

    for x in range(start, stop+1):
        #print("Assessing:\t", x)
        for y in range(1, int((len(str(x)))/2)+1):
            finds = re.finditer(str(x)[0:y], str(x))
            joined_finds = ''.join([x.group() for x in finds])
            if len(joined_finds) == len(str(x)):
                #print("Repeat found in: ", x, str(x)[0:y])
                result += x
                break
    #print("---------------------")

print("Solved problem")
print('Result:\t', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")