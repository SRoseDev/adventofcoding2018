frequencies = dict()
foundDuplicate = False
curF = 0
frequencies[curF] = 1

while not foundDuplicate:
    with open('Day1/day1input.txt') as day1input:
        for frequency in day1input:
            curF = curF + int(frequency)
            fc = frequencies.get(curF, 0)
            if fc > 0:
                print(f'Found Duplicate: {curF}')
                foundDuplicate = True
                break
            else:
                frequencies[curF] = 1

