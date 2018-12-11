from dataclasses import dataclass
from PIL import Image

points = list()


@dataclass
class MessagePoint:
    px: int
    py: int
    vx: int
    vy: int


def plotPointsForTime(t: int):
    p = list()
    maxX = -999999
    maxY = -999999
    minX = 999999
    minY = 999999
    # calculate points for instance in time
    # track bounds
    for point in points:
        newX = point.px + (point.vx * t)
        newY = point.py + (point.vy * t)

        maxX = max(maxX, newX)
        minX = min(minX, newX)
        maxY = max(maxY, newY)
        minY = min(minY, newY)
        p.append(MessagePoint(
            newX,
            newY,
            point.vx,
            point.vy
        ))

    # only print if points are close together
    # print(f'{minX} {maxX} {minY} {maxY}')
    if (maxX - minX) < 150:
        print(f'{minX} {maxX} {minY} {maxY}')
        matrix = [[' ' for y in range(minY, maxY + 1)] for x in range(minX, maxX + 1)]
        print(f'Size for {t}: {maxX - minX + 1} {maxY - minY + 1}')
        for point in p:
            # print(f'Placing {point.px - minX} {point.py - minY}')
            matrix[point.px - minX][point.py - minY] = '#'

        with open(f'{t}output.txt', "w+") as writeFile:
            for row in matrix:
                writeFile.write(str(row))
                writeFile.write('\n')






with open('day10input.txt') as info:
    for line in info:
        s = line.split('>')
        positions = s[0].split('<')[1].split(',')
        velocities = s[1].split('<')[1].split(',')
        points.append(MessagePoint(
            int(positions[0]),
            int(positions[1]),
            int(velocities[0]),
            int(velocities[1])))

print(points)
start = 1000
for t in range(start, start+30000):
    plotPointsForTime(t)