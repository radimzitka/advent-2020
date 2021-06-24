#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         7           #

from os import replace
import re

bags_contain = []

def count_bags(bags, bag_name="shinygold"):
    for bag in bags:
        for bag_in in bag[1:]:
            if(bag_in[1] == bag_name and bag[0] not in bags_contain):
                bags_contain.append(bag[0])
                count_bags(bags, bag[0])

def count_bags_in(bags, bag_name="shinygold"):
    ans = 0
    for bag in bags:
        if(bag[0] == bag_name):
            for bag_in in bag[1:]:
                ans += bag_in[0] + bag_in[0] * count_bags_in(bags, bag_in[1])

    return ans

input = open("input", "r")

# Read file row by row
lines = input.readlines()

bags = []

for line in lines:
    line = line.split(' ')
    bag = [line[0] + line[1]]
    
    if(line[4] == "no"):
        bags.append(bag)
        continue
    
    i = 4
    while(i < len(line)):
        bag.append([int(line[i]), line[i + 1] + line[i + 2]])
        i += 4

    bags.append(bag)

count_bags(bags)
print("Part one:", len(bags_contain))
print("Part two:", count_bags_in(bags))
