c2 = 0
c3 = 0
cl = set()

with open('day2input.txt') as day2input:
    for l in day2input:
        line = l.strip()
        count = dict()
        for c in line:
            count[c] = count.get(c, 0) + 1

        if 2 in count.values():
            cl.add(line)
            c2 = c2+1

        if 3 in count.values():
            cl.add(line)
            c3 = c3+1

sl = sorted(cl)
#reverse and sort the set again to account for first letter being the one that differs
s2 = set()
for s in sl:
    s2.add(s[::-1])

s2 = sorted(s2)

for i in range(len(sl)-1):
    a = sl[i]
    b = sl[i+1]

    #count differences
    diff = 0
    for j in range(len(a)):

        if a[j] != b[j]:
            diff = diff+1

    if diff == 1:
        output = ''
        for k in range(len(a)):
            if a[k] == b[k]:
                output = output.join(a[k])
        print(f'Like letter: {output}')
        break

for i in range(len(s2) - 1):
    a = s2[i]
    b = s2[i+1]
    #count differences
    diff = 0
    for j in range(len(a)-1):
        if a[j] != b[j]:
            diff = diff+1

    if diff == 1:
        output = list()
        print(f'{a[::-1]}\n{b[::-1]}')
        for k in range(len(a)):
            if a[k] == b[k]:
                output.append(a[k])
        print(f'Like letters: {"".join(output[::-1])}')
        break

