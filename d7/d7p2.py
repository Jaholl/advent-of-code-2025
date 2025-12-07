import re
import time
start_time = time.time()

print("Starting problem")
print("---------------------")

#input = open('./d7/sample.txt', 'r').read().split('\n')
input = open('./d7/input.txt', 'r').read().split('\n')
result = 0

#Code starts here

matrix = [list(x) for x in input]

start = matrix[0].index('S')
matrix[0][start] = 1

for x in range(len(matrix)):
    if x == len(matrix)-1:
        break
    for y in range(len(matrix[x])):
        if isinstance(matrix[x][y], int):
            if matrix[x+1][y] == '.':
                matrix[x+1][y] = matrix[x][y]
            elif matrix[x+1][y] == "^":
                if isinstance(matrix[x+1][y-1], int):
                    matrix[x+1][y-1] += matrix[x][y]
                else:
                    matrix[x+1][y-1] = matrix[x][y]
                if isinstance(matrix[x+1][y+1], int):
                    matrix[x+1][y+1] += matrix[x][y]
                else:
                    matrix[x+1][y+1] = matrix[x][y]
            elif isinstance(matrix[x+1][y], int):
                matrix[x+1][y] += matrix[x][y]
                
result = sum([i for i in matrix[-1] if type(i) is int])
#Code ends here

print("Solved problem")
print('Result:\t', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")