#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         8           #

from os import replace

input = open("input", "r")

def run(instructions):
    acc = 0
    p = 0
    while(True):
        if(instructions[p][2] == True):
            return acc, False

        instructions[p][2] = True

        if(instructions[p][0] == 'acc'):
            acc += instructions[p][1]
            p += 1
        elif(instructions[p][0] == 'jmp'):
            p += instructions[p][1]
        elif(instructions[p][0] == 'nop'):
            p += 1

        
        if(p >= len(instructions)):
            return acc, True

    

# Read file row by row
lines = input.readlines()

instructions = []
for line in lines:
    line = line.split(' ')
    instructions.append([line[0], int(line[1]), False])

ans = run(instructions)
print("Part one:", ans[0])

len_ins = len(instructions)
i = 0
while(i < len_ins):
    for instruction in instructions:
        instruction[2] = False

    if(instructions[i][0] == 'jmp'):
        instructions[i][0] = 'nop'
    elif (instructions[i][0] == 'nop'):
        instructions[i][0] = 'jmp'

    ans = run(instructions)

    if(ans[1] == True):
        print("Part two:", ans[0])
        break

    if(instructions[i][0] == 'jmp'):
        instructions[i][0] = 'nop'
    elif (instructions[i][0] == 'nop'):
        instructions[i][0] = 'jmp'

    i += 1
    