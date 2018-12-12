cells = dict()
serial = 1788


def get_power(x, y):
    rackId = x + 10
    power = rackId * y
    power = power + serial
    power = power * rackId
    power = (power % 1000) // 100
    power = power - 5
    return power


def check_square(x, y, s):
    total = 0
    # check 3x3 square starting at this location
    for x1 in range(x, x + s):
        for y1 in range(y, y + s):
            key = f'{x1},{y1}'
            # print(f'checking {key}')
            total = total + cells[key]

    return total


# test power maths
# serial = 57
# print(get_power(122, 79))
#
# serial = 39
# print(get_power(217, 196))
#
# serial = 71
# print(get_power(101, 153))

# build power grid
for x in range(300):
    for y in range(300):
        key = f'{x},{y}'
        cells[key] = get_power(x, y)

largestPower = -999999
largestPowerKey = ''

for s in range(300):
    for x in range(300-s):
        for y in range(300-s):
            total = check_square(x, y, s)
            # print(total)
            if total > largestPower:
                print(f'new Largest {total} as {x},{y},{s}')
                largestPower = total
                largestPowerKey = f'{x},{y},{s}'

print(largestPowerKey)