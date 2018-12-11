import operator

marbleCount = 7206100
playerCount = 428
marbles = list()
marbles.append(0)

curMarble = 1
curMarbleIndex = 0
player = 0
scores = dict()

while not curMarble > marbleCount:
    print(curMarble)
    # divisble by 23
    if curMarble % 23 == 0:
        # player keeps marble
        # get marble 7 places counter-clockwise
        removedIndex = (curMarbleIndex - 7) % (len(marbles))
        m = marbles.pop(removedIndex)
        scores[player] = scores.get(player, 0) + curMarble + m
        # marble at removed index becomes new current
        curMarbleIndex = removedIndex
    # place marble at current + 2 clockwise
    else:
        curMarbleIndex = (curMarbleIndex + 2) % (len(marbles))
        # print(f'New Cur Index: {curMarbleIndex}')
        if curMarbleIndex == 0:
            marbles.append(curMarble)
            curMarbleIndex = len(marbles) - 1
        else:
            marbles.insert(curMarbleIndex, curMarble)

    curMarble = curMarble + 1
    player = (player + 1) % playerCount
    # print(marbles)

print(sorted(scores.items(), key=operator.itemgetter(1), reverse=True))