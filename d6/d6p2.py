import re

rows = open('./d6/input.txt', 'r').read().split('\n')

matrix = []
total = 0

for r in rows:
    matrix.append(list(r))

latest_operation = ''
numbers = []
for x in range(len(matrix[0])):
    column = []
    for y in range(len(matrix)):
        column.append(matrix[y][x])
    print('---------------')
    print(column)

    if column[-1] != ' ':
        latest_operation = column[-1]

    number = ''.join(column[0:-1])
    if number.strip() != '':
        numbers.append(int(number))
    if ''.join(column).strip() == '' or x == len(matrix[0])-1:
        if latest_operation == '*':
            sum = 1
            for num in numbers:
                print(num)
                sum = sum * num
            print(latest_operation)
            print()
            print(sum)
            total += sum
        else:
            sum = 0
            for num in numbers:
                print(num)
                sum += num
            print(latest_operation)
            print()
            print(sum)
            total += sum
        numbers = []
        continue


print('---------------')
print(total)