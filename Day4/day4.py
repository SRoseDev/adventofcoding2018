from datetime import datetime
import operator

events = list()
with open('day4input.txt') as info:
    for line in info:
        dateString = line.split(']')[0].replace('[', '').replace(']', '')
        eventString = line.strip().split(']')[1].strip()
        events.append([datetime.strptime(dateString, "%Y-%m-%d %H:%M"), eventString])

events.sort(key=operator.itemgetter(0))
curGuard = ''
sleepTime = 0
guardSleepCount = dict()
guardSleepMinutes = dict()
for event in events:

    if 'Guard' in event[1]:
        curGuard = event[1].split(' ')[1]

    if 'asleep' in event[1]:
        sleepTime = int(event[0].minute)

    if 'wakes' in event[1]:
        guardSleepCount[curGuard] = guardSleepCount.get(curGuard, 0) + int(event[0].minute) - sleepTime
        for m in range(sleepTime, int(event[0].minute)):
            if curGuard in guardSleepMinutes:
                guardSleepMinutes[curGuard][str(m)] = guardSleepMinutes[curGuard].get(str(m), 0)+1
            else:
                guardSleepMinutes[curGuard] = {}
                guardSleepMinutes[curGuard][str(m)] = guardSleepMinutes[curGuard].get(str(m), 0) + 1
        sleepTime = 0

mostSleep = sorted(guardSleepCount.items(), key=operator.itemgetter(1), reverse=True)
bestGuard = guardSleepMinutes[mostSleep[0][0]]
bestMinute = sorted(bestGuard.items(), key=operator.itemgetter(1), reverse=True)
print(f'Id: {mostSleep[0][0]} minute {bestMinute[0][0]}')




