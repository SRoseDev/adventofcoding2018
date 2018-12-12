import operator
from dataclasses import dataclass


@dataclass
class Marble:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next


marbleCount = 7206100
playerCount = 428

m0 = Marble(0, None, None)
m1 = Marble(1, m0, m0)
m0.prev = m1
m0.next = m1

curMarble = m1
player = 1
scores = dict()

for m in range(2, marbleCount):
    print(m)
    nMarble = Marble(m, None, None)
    player = (player + 1) % playerCount
    # divisble by 23
    if m % 23 == 0:
        # player keeps marble
        # get marble 7 places counter-clockwise
        for x in range(0, 7):
            curMarble = curMarble.prev

        # print(f'7 cc {curMarble.data}')
        # add score
        scores[player] = scores.get(player, 0) + curMarble.data + m
        # do remove
        curMarble.prev.next = curMarble.next
        curMarble.next.prev = curMarble.prev
        # marble at removed index becomes new current
        curMarble = curMarble.next
    # place marble at current + 2 clockwise
    else:
        for x in range(0, 2):
            curMarble = curMarble.next

        # do insert
        nMarble.next = curMarble
        nMarble.prev = curMarble.prev
        nMarble.prev.next = nMarble
        curMarble.prev = nMarble
        curMarble = nMarble

    #print(f'{curMarble.prev.data} {curMarble.data} {curMarble.next.data}')

print(sorted(scores.items(), key=operator.itemgetter(1), reverse=True))