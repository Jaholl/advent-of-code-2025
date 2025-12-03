banks = open('./d3/input.txt', 'r').read().split('\n')

total = 0

for battery_bank in banks:
    if battery_bank == '':
        continue

    print('----------------------')
    print("Assesing bank:\t", battery_bank)
    print()

    found = []

    values = [int(x) for x in battery_bank]
    for x in range(11, 0,-1):
        found.append(max(values[:-x]))
        values = values[values.index(max(values[:-x]))+1:]
    found.append(max(values))
    number = int(''.join([str(x) for x in found]))
    print("Biggest value found:\t", number)
    print()
    total += number


print('----------------------')
print()
print("Result: ", total)