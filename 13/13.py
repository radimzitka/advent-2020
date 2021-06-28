#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         13          #

from math import gcd

input = open("input", "r")    

# Read file row by row
lines = input.readlines()

my_time = int(lines[0])

times = lines[1].split(',')
buses = []

for item in times:
    if(item == 'x'):
        continue
    buses.append(int(item))

wait = buses[0] - my_time % buses[0]

for bus in buses:
    if(wait > bus - my_time % bus):
        wait = bus - my_time % bus
        my_bus = bus

print("Part one:", wait * my_bus)

buses = []
length = len(times)
i = 0
bus = 0

while(i < length):
    if(times[i] == 'x'):
        i += 1
        continue
    else:
        buses.append([int(times[i]), i])
    i += 1

def find_space(one, two, delay, base):
    i = 0
    counter = 0
    count = False
    while(True):
        if((base + one * i + delay) % two == 0 and count == True):
            return base_curr, counter * one
        elif((base + one * i + delay) % two == 0 and count == False):
            count = True
            counter = 0
            base_curr = base + one * i

        counter += 1
        i += 1

space = buses[0][0]
base = 0
for i in range(len(buses) - 1):
    base, space = find_space(space, buses[i + 1][0], buses[i + 1][1], base)

print("Part two:", base)