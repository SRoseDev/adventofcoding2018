from dataclasses import dataclass
import operator


@dataclass
class GridPoint:
    name: str
    x: int
    y: int


def calculate_manhattan_distance(x, y, p: GridPoint):
    return abs(x - p.x) + abs(y - p.y)


points = list()

with open('day6input.txt') as info:
    for line in info:
        thisPoint = GridPoint(
                str(len(points) + 1),
                int(line.split(',')[0]),
                int(line.split(',')[1])
            )
        points.append(thisPoint)

# get grid bounds
xMin = points[0].x
xMax = points[0].x
ymin = points[0].y
yMax = points[0].y

for point in points:
    xMin = min(xMin, point.x)
    xMax = max(xMax, point.x)
    yMin = min(ymin, point.y)
    yMax = max(yMax, point.y)

print(f'{xMin} {xMax} {yMin} {yMax}')
matrix = [['.' for y in range(0, yMax + 100)] for x in range(0, xMax + 100)]

pointCounts = dict()
#Calculate Manhattan Distance, place point, keep count
safeCount = 0
for x in range(0, xMax+100):
    for y in range(0, yMax+100):
        distance = 0
        for point in points:
            distance = distance + calculate_manhattan_distance(x, y, point)

        if distance < 10000:
            safeCount = safeCount + 1

print(safeCount)

