import time
start_time = time.time()

print("Starting problem")
print("---------------------")

#Change x in dx to day number
input = open('./dx/sample.txt', 'r').read().split('\n')
#input = open('./dx/input.txt', 'r').read().split('\n')
result = 0

#Code starts here



#Code ends here

print("Solved problem")
print('Result:\t', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")