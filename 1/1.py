#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         1            #

input = open("input", "r")

# Read file row by row
numbers = input.readlines()

# Convert items to int
numbers = [ int(x) for x in numbers ]

len = len(numbers)
i = 0

while(i < len):
    j = i + 1
    while(j < len):
        if(numbers[i] + numbers[j] == 2020):
            print("Part one: ", numbers[i] * numbers[j])
            i = len
            break
        j += 1
    i += 1

i = j = 0
while(i < len):
    j = i + 1
    while(j < len):
        k = j + 1
        while(k < len):
            if(numbers[i] + numbers[j] + numbers[k] == 2020):
                print("Part two: ", numbers[i] * numbers[j] * numbers[k])
                i = j = len
                break
            k += 1
        j += 1
    i += 1

