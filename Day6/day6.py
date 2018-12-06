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

#place points
for point in points:
    matrix[point.x][point.y] = point.name

pointCounts = dict()
#Calculate Manhattan Distance, place point, keep count
for x in range(0, xMax+100):
    for y in range(0, yMax+100):
        closestPoint = ""
        closestDistance = 999999999
        distances = list()

        for point in points:
            distance = calculate_manhattan_distance(x, y, point)
            distances.append(distance)
            if closestDistance is None or distance < closestDistance:
                closestPoint = point.name
                closestDistance = distance

        distances.sort()
        #check not equal distance from 2 or more points
        if not distances[0] == distances[1]:
            #print(f'Setting {x},{y} to {closestPoint}')
            matrix[x][y] = closestPoint
            pointCounts[closestPoint] = pointCounts.get(closestPoint, 0)+1

infiniteAreaPoints = set()
#walk edge of matrix and add all those points to the infinite list
for x in range(0, xMax+100):
    infiniteAreaPoints.add(matrix[x][0])
    infiniteAreaPoints.add(matrix[x][yMax+99])

for y in range(0, yMax+100):
    infiniteAreaPoints.add(matrix[0][y])
    infiniteAreaPoints.add(matrix[xMax+99][y])

for s in infiniteAreaPoints:
    pointCounts[s] = 0

sortedCounts = sorted(pointCounts.items(), key=operator.itemgetter(1), reverse=True)

print(sortedCounts)

