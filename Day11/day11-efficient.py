# ToDo: Not efficient enough

cells = dict()
serial = 1788

largestPower = -999999
largestPowerKey = ''


def get_power(x, y):
    rackId = x + 10
    power = rackId * y
    power = power + serial
    power = power * rackId
    power = (power % 1000) // 100
    power = power - 5
    return power


def check_square(x, y):
    # starting at x, y walk the grid checking all possible sizes
    global largestPower
    global largestPowerKey
    lastTotal = cells[f'{x},{y}'] #start at 1x1
    for s in range(0, min(300-x,300-y)):
        # print(f'Checking Size {s} for {x},{y}')
        total = lastTotal
        # get next row
        for x1 in range(s):
            key = f'{x+x1},{y+s}'
            total = total + cells[key]

        for y1 in range(s - 1): # don't double count the corner
            key = f'{x+s},{y+y1}'
            total = total + cells[key]

        lastTotal = total
        if total > largestPower:
            print(f'new Largest {total} as {x},{y},{s}')
            largestPower = total
            largestPowerKey = f'{x},{y},{s}'


# build power grid
for x in range(300):
    for y in range(300):
        key = f'{x},{y}'
        cells[key] = get_power(x, y)


for x in range(300):
    for y in range(300):
        check_square(x, y)

print(largestPowerKey)
