rows = open('./d4/input.txt', 'r').read().split('\n')

total = 0

matrix = [list(x) for x in rows]

removed_rolls = -1
while removed_rolls != 0:
    removed_rolls = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            adjacent = 0
            if (matrix[x][y] != "@"):
                continue
            
            #print('----------------------')
            #print()
            #print("Evaluate position:", x, y)
            #print()

            for dx in range(-1,2):
                for dy in range(-1,2):
                    if (dx == dy == 0):
                        continue
                    try:
                        if x + dx < 0 or y + dy < 0:
                            continue
                        if matrix[x+dx][y+dy] != ".":
                            #print("Found adjacent roll in:", x+dx, y+dy)
                            adjacent += 1
                    except:
                        None
            #print()
            #print("Found", adjacent, "adjacent rolls")
            if adjacent < 4:
                matrix[x][y] = '.'
                total += 1
                removed_rolls += 1
            #print()


    #print('----------------------')
    #print()

    #[print(''.join(str(x))) for x in matrix]

print('----------------------')
print()
print("Result:\t", total)