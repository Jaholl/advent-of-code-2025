import time
start_time = time.time()

print("Starting problem")
print("---------------------")

#input = open('./d7/sample.txt', 'r').read().split('\n')
input = open('./d7/input.txt', 'r').read().split('\n')
result = 0

#Code starts here

matrix = [list(x) for x in input]
lines_to_follow = []

start = matrix[0].index('S')
matrix[0][start] = '|'
lines_to_follow.append((0,start))
while lines_to_follow != []:
    current_line = lines_to_follow.pop(0)
    x = current_line[0]
    y = current_line[1]
    if x == len(matrix[0]):
        break
    match matrix[x+1][y]:
        case '.':
            matrix[x+1][y] = '|'
            lines_to_follow.append((x+1,y))
        case '^':
            result += 1
            matrix[x+1][y-1] = '|'
            matrix[x+1][y+1] = '|'
            lines_to_follow.append((x+1,y-1))
            lines_to_follow.append((x+1,y+1))

#Code ends here

print("Solved problem")
print('Result:\t', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")