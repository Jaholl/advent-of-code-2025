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
        length = len(str(x))
        p1 = str(x)[0:int(length/2)]
        p2 = str(x)[int(length/2):]
        if p1 == p2:
            #print("Repeat found in: ", x)
            result += x
    #print("---------------------")

print("Solved problem")
print('Result:\t', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")