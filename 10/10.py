#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         10          #

from os import replace

input = open("input", "r")    

# Read file row by row
lines = input.readlines()

adapters = []
for line in lines:
    adapters.append(int(line))

adapters.append(0)
adapters.sort()

adapters_len = len(adapters)
i = 1
diff_1 = 0
diff_3 = 1

while(i < adapters_len):
    if(adapters[i] - adapters[i - 1] == 1):
        diff_1 += 1
    if(adapters[i] - adapters[i - 1] == 3):
        diff_3 += 1

    i += 1

print("Part one:", diff_1 * diff_3)

set_size = 0
combinations = 1
i = 0

def count_combinations(num):
    if(num == 2):
        return 2
    elif(num == 3):
        return 4
    elif(num == 4):
        return 7

    return 1

for i in range(len(adapters) - 1):
    if(adapters[i + 1] - adapters[i] == 1):
        set_size += 1
        continue

    combinations = combinations * count_combinations(set_size)

    set_size = 0

combinations *= int(count_combinations(set_size))


print("Part two:", combinations)