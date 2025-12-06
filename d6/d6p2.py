import re
import time
start_time = time.time()

print("Starting problem")
print("---------------------")

rows = open('./d6/input.txt', 'r').read().split('\n')

matrix = []
result = 0

for r in rows:
    matrix.append(list(r))

latest_operation = ''
numbers = []
for x in range(len(matrix[0])):
    column = []
    for y in range(len(matrix)):
        column.append(matrix[y][x])
    #print("Evaluating column:",column)

    if column[-1] != ' ':
        latest_operation = column[-1]

    number = ''.join(column[0:-1])
    if number.strip() != '':
        numbers.append(int(number))
    if ''.join(column).strip() == '' or x == len(matrix[0])-1:
        if latest_operation == '*':
            sum = 1
            for num in numbers:
                sum = sum * num
            result += sum
        else:
            sum = 0
            for num in numbers:
                sum += num
            result += sum
        numbers = []
        #print("---------------------")
        continue
    #print("---------------------")

print("Solved problem")
print('Result:\t', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")