from dataclasses import dataclass
from tkinter import *

points = list()
master = Tk()
curTime = 10800
possibleTimes = list()

w = Canvas(master, width=500, height=500)

w.pack()


@dataclass
class MessagePoint:
    px: int
    py: int
    vx: int
    vy: int


def plot_points_for_time(val):
    global curTime
    curTime = int(val)
    print(f'Plotting Time: {val}')
    t = int(val)
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
    if (maxX - minX) < 150 or (maxY - minY) < 150:
        # print(f'{minX} {maxX} {minY} {maxY}')
        global possibleTimes
        possibleTimes.append(t)

        w.delete("all")

        for point in p:
            # print(f'Placing {point.px - minX} {point.py - minY}')
            w.create_line(point.px, point.py, point.px+1, point.py+1, fill="#ff0000")

        w.update()


def check_points_for_time(val):
    t = int(val)
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
    if (maxX - minX) < 150 or (maxY - minY) < 150:
        # print(f'{minX} {maxX} {minY} {maxY}')
        global possibleTimes
        possibleTimes.append(t)

        w.delete("all")

        for point in p:
            # print(f'Placing {point.px - minX} {point.py - minY}')
            w.create_line(point.px, point.py, point.px+1, point.py+1, fill="#ff0000")

        w.update()


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

# loop once to get bounds
for t in range(10000, 20000):
    check_points_for_time(t)

possibleTimes.sort()
s = Scale(master, from_=possibleTimes[0], to=possibleTimes[len(possibleTimes) - 1], length=300, orient=HORIZONTAL, command=plot_points_for_time)
s.pack()


mainloop()