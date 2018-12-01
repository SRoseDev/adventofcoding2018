curF = 0

with open('day1input.txt') as day1input:
    for frequency in day1input:
        curF = curF + int(frequency)

print(f'Frequency: {curF}')
