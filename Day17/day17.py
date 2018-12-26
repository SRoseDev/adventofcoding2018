import re

soil = dict()
minX = float('inf')
maxX = float('-inf')
minY = float('inf')
maxY = float('-inf')


def printSoil():
    global minX, maxX, minY, maxY
    for y in range(minY - 1, maxY + 2):
        l = ''
        for x in range(minX - 1, maxX + 2):
            key = f'{x},{y}'
            l = l+soil.get(key, '.')

        print(l)

    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')
    print(' ')


#get input
with open('day17-input.txt') as info:
    for line in info:
        parts = line.split(' ')
        if parts[0][0] == 'x':
            x =int(re.findall('\\d+', parts[0])[0])
            if x < minX:
                minX = x
            if x > maxX:
                maxX = x

            r = list(map(int, re.findall('\\d+', parts[1])))
            for y in range(r[0], r[1]+1):
                if y > maxY:
                    maxY = y
                if y < minY:
                    minY = y

                key = f'{x},{y}'
                soil[key] = '#'

        else:
            y = int(re.findall('\\d+', parts[0])[0])
            if y < minY:
                minY = y
            if y > maxY:
                maxY = y

            r = list(map(int, re.findall('\\d+', parts[1])))
            for x in range(r[0], r[1]+1):
                if x > maxX:
                    maxX = x
                if x < minX:
                    minX = x

                key = f'{x},{y}'
                soil[key] = '#'

soil['500,0'] = '+'
waterPos = list()
# x, y, direction
waterPos.append([500, 0, 1])
canFlow = True

while canFlow:
    # check next tick
    # printSoil()
    for water in waterPos:
        # flow down
        if water[2] == 1:
            # check for end
            if water[1] == maxY:
                water[2] = 0
                shouldContinue = False
                for w in waterPos:
                    if not w[2] == 0:
                        shouldContinue = True
                canFlow = shouldContinue
                continue

            if soil.get(f'{water[0]},{water[1]+water[2]}', '.') == '.':
                soil[f'{water[0]},{water[1]+water[2]}'] = '|'
                water[1] = water[1] + water[2]
            # flow out
            elif soil.get(f'{water[0]},{water[1]+water[2]}', '.') == '#':
                # check if contained
                print("hit soil")
                cLeft = False
                bLeft = minX - 1
                cRight = False
                bRight = maxX + 1
                for x in range(water[0], minX-1, -1):
                    if soil.get(f'{x},{water[1]}', '.') == '#':
                        print(f' hit left at {x}')
                        bLeft = x
                        cLeft = True
                        break
                    if soil.get(f'{x},{water[1]+1}', '.') == '.':
                        break

                for x in range(water[0], maxX+1):
                    if soil.get(f'{x},{water[1]}', '.') == '#':
                        print(f'hit right at {x}')
                        bRight = x
                        cRight = True
                        break
                    if soil.get(f'{x},{water[1]+1}', '.') == '.':
                        break

                if cLeft and cRight:
                    # water is contained
                    print("Water Contained")
                    for x in range(bLeft + 1, bRight):
                        key = f'{x},{water[1]}'
                        soil[key] = '~'

                    water[2] = -1
                    water[1] = water[1] - 1

                else:
                    water[2] = 0  # stop flow at this node
                    # flow right
                    if not cRight:
                        x = water[0]
                        while soil.get(f'{x},{water[1]+1}', '.') == '#' or soil.get(f'{x},{water[1]+1}', '.') == '~':
                            soil[f'{x},{water[1]}'] = '|'
                            x = x + 1

                        # add new water node
                        soil[f'{x},{water[1]}'] = '|'
                        waterPos.append([x, water[1], 1])
                    else:
                        for x in range(water[0], bRight):
                            key = f'{x},{water[1]}'
                            soil[key] = '~'

                    # flow left
                    if not cLeft:
                        x = water[0]
                        while soil.get(f'{x},{water[1]+1}', '.') == '#' or soil.get(f'{x},{water[1]+1}', '.') == '~':
                            soil[f'{x},{water[1]}'] = '|'
                            x = x - 1

                        # add new water node
                        soil[f'{x},{water[1]}'] = '|'
                        waterPos.append([x, water[1], 1])
                    else:
                        for x in range(water[0], bLeft, -1):
                            key = f'{x},{water[1]}'
                            soil[key] = '~'

        elif water[2] == -1:
            # flow up
            #check contained
            cLeft = False
            bLeft = minX - 1
            cRight = False
            bRight = maxX + 1
            for x in range(water[0], minX - 1, -1):
                if soil.get(f'{x},{water[1]}', '.') == '#':
                    print(f'hit left at {x}')
                    bLeft = x
                    cLeft = True
                    break
                if soil.get(f'{x},{water[1]+1}', '.') == '.':
                    break

            for x in range(water[0], maxX + 1):
                if soil.get(f'{x},{water[1]}', '.') == '#':
                    print(f'hit right at {x}')
                    bRight = x
                    cRight = True
                    break
                if soil.get(f'{x},{water[1]+1}', '.') == '.':
                    break

            if cLeft and cRight:
                # water is contained
                print("Water Contained")
                for x in range(bLeft + 1, bRight):
                    key = f'{x},{water[1]}'
                    soil[key] = '~'

                water[2] = -1
                water[1] = water[1] - 1

            else:
                water[2] = 0 #stop flow at this node
                # flow right
                if not cRight:
                    x = water[0]
                    while soil.get(f'{x},{water[1]+1}', '.') == '#' or soil.get(f'{x},{water[1]+1}', '.') == '~':
                        soil[f'{x},{water[1]}'] = '|'
                        x = x+1

                    # add new water node
                    soil[f'{x},{water[1]}'] = '|'
                    waterPos.append([x, water[1], 1])
                else:
                    for x in range(water[0], bRight):
                        key = f'{x},{water[1]}'
                        soil[key] = '|'

                # flow left
                if not cLeft:
                    x = water[0]
                    while soil.get(f'{x},{water[1]+1}', '.') == '#' or soil.get(f'{x},{water[1]+1}', '.') == '~':
                        soil[f'{x},{water[1]}'] = '|'
                        x = x - 1

                    # add new water node
                    soil[f'{x},{water[1]}'] = '|'
                    waterPos.append([x, water[1], 1])
                else:
                    for x in range(water[0], bLeft, -1):
                        key = f'{x},{water[1]}'
                        soil[key] = '|'

# count water blocks
water_count = 0
for b in soil.values():
    if not b == '.' and not b =='#' and not b == '+':
        water_count = water_count + 1

print(water_count)