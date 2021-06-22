#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         2           #

input = open("input", "r")

# Read file row by row
lines = input.readlines()

len = len(lines)
occ_counter_one = occ_counter_two = 0

for line in lines:
    by_spaces = line.split(' ')
    min = int(by_spaces[0].split('-')[0])
    max = int(by_spaces[0].split('-')[1])
    char = by_spaces[1][0]
    password = by_spaces[2]

    count = password.count(char)

    if(count >= min and count <= max):
        occ_counter_one += 1
    
    if(password[min - 1] == char and password[max - 1] != char or password[min - 1] != char and password[max - 1] == char):
        occ_counter_two += 1

print("Part one: ", occ_counter_one)
print("Part two: ", occ_counter_two)
