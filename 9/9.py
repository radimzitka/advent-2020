#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         9           #

from os import replace

input = open("input", "r")    

# Read file row by row
lines = input.readlines()

nums = []
for line in lines:
    nums.append(int(line))


def find_sum(nums, founded, preamble):
    i = 0
    while(i < preamble):
        j = i + 1
        while(j < preamble):
            if(nums[i] + nums[j] == founded):
                return True
            
            j += 1
        i += 1

    return False

preamble = 25
range_min = 0
range_max = preamble
invalid = 0

for num in nums[preamble:]:
    if(find_sum(nums[range_min:range_max], nums[range_max], preamble) == False):
        invalid = nums[range_max]
        print("Part one:", nums[range_max])
        break
    
    range_min += 1
    range_max += 1

set_size = 2
nums_len = len(nums)
i = 0

def find_min_max(arr):
    min = max = arr[0]

    for item in arr:
        if(item > max):
            max = item
        if(item < min):
            min = item
        
    return min, max

while(True):
    while(i + set_size < nums_len):
        total = 0
        for j in range(set_size):
            total += nums[i + j]

        if(total == invalid):
            min, max = find_min_max(nums[i:i + set_size])
            print("Part two:", min + max)
            exit(0)
        i += 1

    set_size += 1
    i = 0