#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         5           #

from os import replace
import re


input = open("input", "r")

# Read file row by row
lines = input.readlines()

max = 0
ids = []
for line in lines:
    interval_max = 128
    interval_min = 0
    interval_max_seat = 8
    interval_min_seat = 0
    i = 0

    while (i < 10):
        if(line[i] == 'F'):
            interval_max = (interval_max - interval_min) / 2 + interval_min
        elif(line[i] == 'B'):
            interval_min = (interval_max - interval_min) / 2 + interval_min

        elif(line[i] == 'L'):
            interval_max_seat = (interval_max_seat - interval_min_seat) / 2 + interval_min_seat
        elif(line[i] == 'R'):
            interval_min_seat = (interval_max_seat - interval_min_seat) / 2 + interval_min_seat
        i += 1
    
    if(max < interval_min * 8 + interval_min_seat):
        max = interval_min * 8 + interval_min_seat

    ids.append(interval_min * 8 + interval_min_seat)
    

print("Part one:", int(max))

ids.sort()

first = ids[0]
for i in range(len(ids)):
    if(ids[i] != first):
        print("Part two:", int(first))
        break
    
    first += 1
