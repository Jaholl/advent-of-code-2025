import time
start_time = time.time()

print("Starting problem")
print("---------------------")

rows = open('./d4/input.txt', 'r').read().split('\n')

result = 0

matrix = [list(x) for x in rows]

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        adjacent = 0
        if (matrix[x][y] != "@"):
            continue
        
        #print("Evaluate position:", x, y)

        for dx in range(-1,2):
            for dy in range(-1,2):
                if (dx == dy == 0):
                    continue
                try:
                    if x + dx < 0 or y + dy < 0:
                        continue
                    if matrix[x+dx][y+dy] != ".":
                        adjacent += 1
                except:
                    None
        matrix[x][y] = adjacent
        if adjacent < 4:
            result += 1
        #print("---------------------")

print("Solved problem")
print('Result:\t', result)
print("Execution time: %s ms" % (round(((time.time() - start_time)*1000), 2)))
print("---------------------")