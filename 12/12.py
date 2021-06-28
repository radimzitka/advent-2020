#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         12          #

input = open("input", "r")    

# Read file row by row
lines = input.readlines()

position = [0, 0] # x, y

curr_way = 0

ways = ['E', 'S', 'W', 'N']

def shift_way(dist, pos):
    pos += dist
    if(pos < 0):
        pos += 4
    
    if(pos > 3):
        pos -= 4

    return pos     

def move(distance, direction, position):
    if(direction == 'E'):
        position[0] += distance
    if(direction == 'S'):
        position[1] -= distance
    if(direction == 'W'):
        position[0] -= distance
    if(direction == 'N'):
        position[1] += distance

    return position

def round(arr, about):
    if(about >= 0):
        for i in range(about):
            x = arr[0]
            arr[0] = arr[1]
            arr[1] = x * (-1)

    else:
        for i in range(abs(about)):
            x = arr[0]
            arr[0] = arr[1] * (-1)
            arr[1] = x

    return arr

for line in lines:
    if(line[0] == 'N' or line[0] == 'E' or line[0] == 'S' or line[0] == 'W'):
        position = move(int(line[1:]), line[0], position)
    elif(line[0] == 'F'):
        position = move(int(line[1:]), ways[curr_way], position)
    elif(line[0] == 'L'):
        curr_way = shift_way(int(int(line[1:]) / 90 % 4 * (-1) ) , curr_way)
    elif(line[0] == 'R'):
        curr_way = shift_way(int(int(line[1:]) / 90 % 4), curr_way)
    
print("Part one: ", abs(position[0])  + abs(position[1]))

way_point = [10, 1]
position = [0, 0] # x, y

for line in lines:
    if(line[0] == 'N' or line[0] == 'E' or line[0] == 'S' or line[0] == 'W'):
        way_point = move(int(line[1:]), line[0], way_point)
    elif(line[0] == 'F'):
        position[0] += int(line[1:]) * way_point[0]
        position[1] += int(line[1:]) * way_point[1]
    elif(line[0] == 'L'):
        way_point = round(way_point, int(int(line[1:]) / 90 % 4 * (-1) ))
    elif(line[0] == 'R'):
        curr_way = round(way_point, int(int(line[1:]) / 90 % 4))

print("Part two: ", abs(position[0])  + abs(position[1]))

