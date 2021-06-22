#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         3           #

input = open("input", "r")

# Read file row by row
lines = input.readlines()

line_len = len(lines[0]) - 1 # Withnout new line character

pos = 0
counter = 0
for line in lines:
    if(line[pos % line_len] == '#'):
        counter += 1
    pos += 3
print("Part one: ", counter)

move_arr = [[1,1], [3,1], [5,1], [7,1], [1,2]]
counter = i = pos = 0
ans = 1
lines_len = len(lines)

for arr_i in range(len(move_arr)):
    while(i < lines_len):
        if(lines[i][pos % line_len] == '#'):
            counter += 1
        i += move_arr[arr_i][1]
        pos += move_arr[arr_i][0]

    ans = ans * counter
    i = pos = counter = 0

print("Part two: ", ans)