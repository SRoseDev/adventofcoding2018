c2 = 0
c3 = 0

with open('day2input.txt') as day2input:
    for line in day2input:
        count = dict()
        for c in line:
            count[c] = count.get(c, 0) + 1

        if 2 in count.values():
            print(f'found 2 in {line}')
            c2 = c2+1

        if 3 in count.values():
            print(f'found 3 in {line}')
            c3 = c3+1

print(f'contains 2: {c2} contains 3: {c3} checksum: {c2 * c3}')
