#    Advent of code 2020    #
# Author:       Radim Zitka #
# Task:         17          #

input = open("input", "r")    

# Read file row by row
lines = input.readlines()

def surroundings_active_4D(pocket, w, x, y, z):
    counter = 0
    if(pocket[w][z][y][x] == '#'):
        counter = -1

    x += 2
    y += 2
    z += 2
    w -= 1

    for i in range(3):
        z -= 3
        for i in range(3):
            y -= 3
            for j in range(3):
                x -= 3
                for k in range(3):
                    if(w >= len(pocket) or z >= len(pocket[w]) or y >= len(pocket[w][z]) or x >= len(pocket[w][z][y])):
                        pass
                    elif(w < 0 or z < 0 or y < 0 or x < 0):
                        pass
                    elif(pocket[w][z][y][x] == '#'):
                        counter += 1
                    x += 1
                y += 1
            z += 1
        w += 1
    return counter

def surroundings_active_3D(pocket, x, y, z):
    counter = 0
    if(pocket[z][y][x] == '#'):
        counter = -1

    x += 2
    y += 2
    z -= 1

    for i in range(3):
        y -= 3
        for j in range(3):
            x -= 3
            for k in range(3):
                if(z >= len(pocket) or y >= len(pocket[0]) or x >= len(pocket[0][0])):
                    pass
                elif(z < 0 or y < 0 or x < 0):
                    pass
                elif(pocket[z][y][x] == '#'):
                    counter += 1
                x += 1
            y += 1
        z += 1

    return counter

def make_pocket_bigger(pocket, _4D = False):
    if(_4D == False):
        new = []
        new.append(pocket)
        pocket = new

    for i in range(len(pocket)):
        for slice in pocket[i]:
            for line in slice:
                line.append('.')
                line.insert(0,'.')
            slice.insert(0, [ '.' for i in range(len(slice[0])) ])
            slice.append([ '.' for i in range(len(slice[0])) ])

        front = [ [ '.' for i in range(len(pocket[0][0])) ] for j in range(len(pocket[0][0])) ]
        pocket[i].insert(0, front)
        pocket[i].append(front[:])

    if(_4D):
        front = [[['.' for _x in range(len(pocket[0][0][0]))] for _y in range(len(pocket[0][0]))] for _z in range(len(pocket[0]))]
        pocket.append(front)
        pocket.insert(0, front[:])
    else:
        pocket = pocket[0]

def no_active_edges(pocket, _4D = False):
    if(_4D == False):
        new = []
        new.append(pocket)
        pocket = new

    for i in range(len(pocket)):
        if any('#' in x for x in pocket[i][0]): # First slice
            return False
        if any('#' in x for x in pocket[i][-1]): # Last slice
            return False
        for slice in pocket[i][1:-1]:
            if('#' in slice[0] or '#' in slice[-1]): # First/Last row for every slice
                return False
            for row in slice[1:-2]:
                if(row[0] == '#' or row[-1] == '#'):
                    return False

    return True

def cycle_3D(pocket):
    while(True):
        z = 0
        
        new_pocket = [[['.' for _x in range(len(pocket[0][0]))] for _y in range(len(pocket[0]))] for _z in range(len(pocket))]
        while(z < len(pocket)):
            x = y = 1
            while(y < len(pocket[0])):
                x = 1
                while(x < len(pocket[0][0])):
                    surroundings = surroundings_active_3D(pocket, x, y, z)
                    if(pocket[z][y][x] == '#' and surroundings != 2 and surroundings != 3):
                        new_pocket[z][y][x] = '.'

                    elif(pocket[z][y][x] == '.' and surroundings == 3):
                        new_pocket[z][y][x] = '#'

                    else:
                        new_pocket[z][y][x] = pocket[z][y][x]
                    x += 1
                y += 1
            z += 1

        if(no_active_edges(new_pocket[:])):
            break    
        else:
            make_pocket_bigger(pocket)

    return new_pocket

def cycle_4D(pocket):
    while(True):
        w = 0
        new_pocket = [[[['.' for _x in range(len(pocket[w][0][0]))] for _y in range(len(pocket[w][0]))] for _z in range(len(pocket[w]))] for _z in range(len(pocket))]

        while(w < len(pocket)):
            z = 0
            while(z < len(pocket[0])):
                x = y = 1
                while(y < len(pocket[0][0])):
                    x = 1
                    while(x < len(pocket[0][0][0])):
                        surroundings = surroundings_active_4D(pocket, w, x, y, z)
                        if(pocket[w][z][y][x] == '#' and surroundings != 2 and surroundings != 3):
                            new_pocket[w][z][y][x] = '.'

                        elif(pocket[w][z][y][x] == '.' and surroundings == 3):
                            new_pocket[w][z][y][x] = '#'

                        else:
                            new_pocket[w][z][y][x] = pocket[w][z][y][x]
                        x += 1
                    y += 1
                z += 1
            w += 1

        if(no_active_edges(new_pocket[:], True)):
            break    
        else:
            make_pocket_bigger(pocket, True)
                

    return new_pocket
    



z_slice = []
pocket_3D = []
pocket_4D = []

for line in lines:
    row = []
    for char in line:
        if(char == '\n'):
            continue
        row.append(char)

    z_slice.append(row)

pocket_3D.append(z_slice[:])
pocket_4D.append(pocket_3D[:])


for i in range(6):
    pocket_3D = cycle_3D(pocket_3D)
    pocket_4D = cycle_4D(pocket_4D)

sum = 0
for slice in pocket_3D:
    for row in slice:
        sum += row.count('#')
print("Part one:", sum)

sum = 0
for box in pocket_4D:
    for slice in box:
        for row in slice:
            sum += row.count('#')
print("Part two:", sum)


