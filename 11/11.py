#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         11          #

from copy import copy, deepcopy

input = open("input", "r")    

# Read file row by row
lines = input.readlines()

lines = [line.replace('\n', '') for line in lines]
lines = ['.' + line for line in lines]
lines = [line + '.' for line in lines]
lines.append('.' * len(lines[0]))
lines.insert(0, '.' * len(lines[0]))
lines = [list(line) for line in lines]



def check_surrounding(task, arr, x, y):
    occupy = 0

    if(task == 1):
        if(arr[y][x+1] == '#'):
            occupy += 1
        if(arr[y+1][x+1] == '#'):
            occupy += 1
        if(arr[y+1][x] == '#'):
            occupy += 1
        if(arr[y+1][x-1] == '#'):
            occupy += 1
        if(arr[y][x-1] == '#'):
            occupy += 1
        if(arr[y-1][x-1] == '#'):
            occupy += 1
        if(arr[y-1][x] == '#'):
            occupy += 1
        if(arr[y-1][x+1] == '#'):
            occupy += 1

    if(task == 2):
        i = 0
        while(x+1+i < len(arr[0])):
            if(arr[y][x+1+i] == '#'):
                occupy += 1
                break
            if(arr[y][x+1+i] == 'L'):
                break
            i += 1

        i = 0
        while(y+1+i < len(arr) and x+1+i < len(arr[0])):    
            if(arr[y+1+i][x+1+i] == '#'):
                occupy += 1
                break
            if(arr[y+1+i][x+1+i] == 'L'):
                break
            i += 1

        i = 0
        while(y+1+i < len(arr)):  
            if(arr[y+1+i][x] == '#'):
                occupy += 1
                break
            if(arr[y+1+i][x] == 'L'):
                break
            i += 1

        i = 0
        while(y+1+i < len(arr) and x-1-i > 0):  
            if(arr[y+1+i][x-1-i] == '#'):
                occupy += 1
                break
            if(arr[y+1+i][x-1-i] == 'L'):
                break
            i += 1

        i = 0
        while(x-1-i > 0):  
            if(arr[y][x-1-i] == '#'):
                occupy += 1
                break
            if(arr[y][x-1-i] == 'L'):
                break
            i += 1

        i = 0
        while(y-1-i > 0 and x-1-i > 0):  
            if(arr[y-1-i][x-1-i] == '#'):
                occupy += 1
                break
            if(arr[y-1-i][x-1-i] == 'L'):
                break
            i += 1

        i = 0
        while(y-1-i > 0):  
            if(arr[y-1-i][x] == '#'):
                occupy += 1
                break
            if(arr[y-1-i][x] == 'L'):
                break
            i += 1
        i = 0

        while(y-1-i > 0 and x+1+i < len(arr[0])):  
            if(arr[y-1-i][x+1+i] == '#'):
                occupy += 1
                break
            if(arr[y-1-i][x+1+i] == 'L'):
                break
            i += 1
            
    return occupy



def task(task, old_arr, new_arr):
    seats = len(old_arr[0])
    while(True):
        change = False
        i = j = 1
        while(i < rows - 1):
            while(j < seats - 1):
                occupy = check_surrounding(task, old_arr, j, i)
                #print(occupy)
                if(occupy == 0 and old_arr[i][j] == 'L'):
                    new_arr[i][j] = '#'
                    change = True
                if(old_arr[i][j] == '#' and (task == 1 and occupy >= 4 or task == 2 and occupy >= 5)):
                    new_arr[i][j] = 'L'
                    change = True

                j += 1
            i += 1
            j = 1

        old_arr = deepcopy(new_arr)

        if(change == False):
            count = 0
            for seats in old_arr:
                count += seats.count("#")
            
            if(task == 1):
                print("Part one:", count)
            if(task == 2):
                print("Part two:", count)
            return

seats = len(lines[0])
rows = len(lines)
old_seats = deepcopy(lines)
new_seats = [['.' for x in range(seats)] for y in range(rows)] 

i = j = 1

task(1, old_seats, new_seats)

new_seats = [['.' for x in range(seats)] for y in range(rows)]
task(2, lines, new_seats)