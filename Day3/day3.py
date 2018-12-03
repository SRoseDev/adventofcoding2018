#count overlapping squares
squares = dict()

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

overlap = 0
for v in squares.values():
    if v > 1:
        overlap = overlap+1

print(overlap)

