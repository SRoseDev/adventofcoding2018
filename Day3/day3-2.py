#count overlapping squares
squares = dict()

#build squares
with open ('day3input.txt') as info:
    #get x,y and add as key to dict
    for line in info:
        sections = line.split(' ')
        cords = sections[2].replace(':', '').split(',')
        dims = sections[3].split('x')

        for x in range(int(cords[0]), int(cords[0])+int(dims[0])):
            for y in range(int(cords[1]), int(cords[1]) + int(dims[1])):
                key = str(x)+','+str(y)
                squares[key] = squares.get(key, 0)+1

#check squares for overlap
with open ('day3input.txt') as info:
    #get x,y and add as key to dict
    for line in info:
        sections = line.split(' ')
        cords = sections[2].replace(':', '').split(',')
        dims = sections[3].split('x')
        id = sections[0]
        hasOverlap = False
        for x in range(int(cords[0]), int(cords[0])+int(dims[0])):
            for y in range(int(cords[1]), int(cords[1]) + int(dims[1])):
                key = str(x)+','+str(y)
                if squares[key] != 1:
                    hasOverlap = True
                    break
            if hasOverlap:
                break

        if not hasOverlap:
            print(id)
            break
