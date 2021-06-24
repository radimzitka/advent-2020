#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         6           #

from os import replace


input = open("input", "r")

# Read file row by row
lines = input.read().split('\n\n')

ans = 0

lines_1 = [line.replace('\n', '') for line in lines]
lines_1 = ["".join(set(line)) for line in lines_1]
for line in lines_1:
    ans += len(line)

print("Part one:", ans)

ans = 0

for line in lines:
    line = line.split('\n')

    found = True
    for char in line[0]:
        for answer in line[1:]:
            if(char not in answer):
                found = False
                break
        if(found):
            ans += 1
        found = True

print("Part two:", ans)