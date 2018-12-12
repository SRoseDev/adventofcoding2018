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


def check_square(x, y):
    total = 0
    # check 3x3 square starting at this location
    for x1 in range(x, x + 3):
        for y1 in range(y, y + 3):
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

for x in range(297):
    for y in range(297):
        total = check_square(x, y)
        # print(total)
        if total > largestPower:
            print(f'new Largest {total} as {x},{y}')
            largestPower = total
            largestPowerKey = f'{x},{y}'

print(largestPowerKey)