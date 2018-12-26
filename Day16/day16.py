from dataclasses import dataclass
import re
# I didn't understand this one so I got help from the internet. Now I understand

@dataclass
class Operation:
    def __init__(self, before, op, after):
        self.before = before
        self.op = op
        self.after = after


operations = list()
#read input
input_index = 0
before = None
after = None
op = None

with open('day16-input.txt') as info:
    for line in info:
        if input_index % 4 == 0:
            before = list(map(int, re.findall('\\d+', line)))
        elif input_index % 4 == 1:
            op = list(map(int, re.findall('\\d+', line)))
        elif input_index % 4 == 2:
            after = list(map(int, re.findall('\\d+', line)))
            operations.append(Operation(before, op, after))

        input_index = input_index + 1

more_than_three_ops = 0
for test in operations:
    op_count = 0

    rops = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr',
            'eqir', 'eqri', 'eqrr']

    if test.after[test.op[3]] != (test.before[test.op[1]] + test.op[2]):
        rops.remove('addi')
    if test.after[test.op[3]] != (test.before[test.op[1]] + test.before[test.op[2]]):
        rops.remove('addr')
    if test.after[test.op[3]] != (test.before[test.op[1]] * test.op[2]):
        rops.remove('muli')
    if test.after[test.op[3]] != (test.before[test.op[1]] * test.before[test.op[2]]):
        rops.remove('mulr')
    if test.after[test.op[3]] != (test.before[test.op[1]] & test.op[2]):
        rops.remove('bani')
    if test.after[test.op[3]] != (test.before[test.op[1]] & test.before[test.op[2]]):
        rops.remove('banr')
    if test.after[test.op[3]] != (test.before[test.op[1]] | test.op[2]):
        rops.remove('bori')
    if test.after[test.op[3]] != (test.before[test.op[1]] | test.before[test.op[2]]):
        rops.remove('borr')
    if test.after[test.op[3]] != test.op[1]:
        rops.remove('seti')
    if test.after[test.op[3]] != test.before[test.op[1]]:
        rops.remove('setr')
    if (test.op[1] > test.before[test.op[2]] and test.after[test.op[3]] != 1) or (
            test.op[1] <= test.before[test.op[2]] and test.after[test.op[3]] != 0):
        rops.remove('gtir')
    if (test.before[test.op[1]] > test.op[2] and test.after[test.op[3]] != 1) or (
            test.before[test.op[1]] <= test.op[2] and test.after[test.op[3]] != 0):
        rops.remove('gtri')
    if (test.before[test.op[1]] > test.before[test.op[2]] and test.after[test.op[3]] != 1) or (
            test.before[test.op[1]] <= test.before[test.op[2]] and test.after[test.op[3]] != 0):
        rops.remove('gtrr')
    if (test.op[1] == test.before[test.op[2]] and test.after[test.op[3]] != 1) or (
            test.op[1] != test.before[test.op[2]] and test.after[test.op[3]] != 0):
        rops.remove('eqir')
    if (test.before[test.op[1]] == test.op[2] and test.after[test.op[3]] != 1) or (
            test.before[test.op[1]] != test.op[2] and test.after[test.op[3]] != 0):
        rops.remove('eqri')
    if (test.before[test.op[1]] == test.before[test.op[2]] and test.after[test.op[3]] != 1) or (
            test.before[test.op[1]] != test.before[test.op[2]] and test.after[test.op[3]] != 0):
        rops.remove('eqrr')

    if len(rops) >= 3:
        more_than_three_ops = more_than_three_ops + 1

print(more_than_three_ops)