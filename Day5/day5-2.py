def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)

with open('day5input.txt', 'r') as info:
    data = info.read().replace('\n', '')
    bestLength = len(data)

    for r in char_range('a', 'z'):
        curString = data.replace(r, '').replace(r.upper(), '')
        lastLen = 0
        startLen = len(curString)

        while not startLen == lastLen:
            startLen = len(curString)
            for c in char_range('a', 'z'):
                r1 = f'{c}{c.upper()}'
                r2 = f'{c.upper()}{c}'
                curString = curString.replace(r1, '').replace(r2, '')
            lastLen = len(curString)

        curlen = len(curString)
        if curlen < bestLength:
            bestLength = curlen

print(bestLength)
