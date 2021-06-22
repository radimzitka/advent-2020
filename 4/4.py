#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         3           #

from os import replace
import re


input = open("input", "r")

# Read file row by row
lines = input.read().split('\n\n')

lines = [line.replace('\n', ' ') for line in lines]

pass_counter = 0
pass_valid_counter = 0

for line in lines:
    pass_fields = line.split(' ')

    values = [field[4:] for field in pass_fields]
    items = [field[:3] for field in pass_fields]

    valid = False
    if(len(items) == 8 or (len(items) == 7 and 'cid' not in items)):
        pass_counter += 1
        valid = True

    i = -1
    for item in items:
        i += 1
        if(item == 'byr' and int(values[i]) >= 1920 and int(values[i]) <= 2002):
            continue
        elif(item == 'iyr' and int(values[i]) >= 2010 and int(values[i]) <= 2020):
            continue
        elif(item == 'eyr' and int(values[i]) >= 2020 and int(values[i]) <= 2030):
            continue
        elif(item == 'hgt'):
            if(values[i][-2:] == 'cm' and int(values[i][:-2]) >= 150 and int(values[i][:-2]) <= 193):
                continue
            elif(values[i][-2:] == 'in' and int(values[i][:-2]) >= 59 and int(values[i][:-2]) <= 76):
                continue
            else:
                valid = False
                break
        elif(item == 'hcl' and re.match('\#[a-f0-9]{6}$', values[i])):
            continue
        elif(item == 'ecl' and (values[i] == 'amb' or values[i] == 'blu' or values[i] == 'brn' or values[i] == 'gry' or values[i] == 'grn' or
            values[i] == 'hzl' or values[i] == 'oth')):
            continue
        elif(item == 'pid' and re.match('[0-9]{9}$', values[i])):
            continue
        elif(item == 'cid'):
            continue
        else:
            valid = False
            break

    if(valid):
        pass_valid_counter += 1

print("Part one:", pass_counter)
print("Part two:", pass_valid_counter)
    