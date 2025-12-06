import time
start_time = time.time()

print("Starting problem")
print("---------------------")

banks = open('./d3/input.txt', 'r').read().split('\n')

result = 0

for battery_bank in banks:
    if battery_bank == '':
        continue

    #print("Assesing bank:\t", battery_bank)

    found = []

    values = [int(x) for x in battery_bank]
    found.append(max(values[:-1]))
    values = values[values.index(max(values[:-1]))+1:]
    found.append(max(values))
    number = int(''.join([str(x) for x in found]))
    #print("Biggest value found:\t", number)
    result += number
    #print("---------------------")

print("Solved problem")
print('Result:\t', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")