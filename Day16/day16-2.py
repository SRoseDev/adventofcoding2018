from dataclasses import dataclass
import re
# I didn't understand this one so I got help from the internet. Now I understand

@dataclass
class Operation:
    def __init__(self, before, op, after):
        self.before = before
        self.op = op
        self.after = after


def remove_op(op, index):
    global ops
    if op in ops[index]:
        ops[index].remove(op)


rops = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti', 'gtir', 'gtri', 'gtrr', 'eqir', 'eqri', 'eqrr']

ops = {}
for i in range(len(rops)):
    ops[i] = list(rops)

print(ops)

operations = list()
#read input
input_index = 0

with open('day16-input.txt') as info:
    before = None
    after = None
    op = None
    for line in info:
        if input_index % 4 == 0:
            before = list(map(int, re.findall('\\d+', line)))
        elif input_index % 4 == 1:
            op = list(map(int, re.findall('\\d+', line)))
        elif input_index % 4 == 2:
            after = list(map(int, re.findall('\\d+', line)))
            operations.append(Operation(before, op, after))

        input_index = input_index + 1


for test in operations:

    if test.after[test.op[3]] != (test.before[test.op[1]] + test.op[2]):
        remove_op('addi', test.op[0])
    if test.after[test.op[3]] != (test.before[test.op[1]] + test.before[test.op[2]]):
        remove_op('addr', test.op[0])
    if test.after[test.op[3]] != (test.before[test.op[1]] * test.op[2]):
        remove_op('muli', test.op[0])
    if test.after[test.op[3]] != (test.before[test.op[1]] * test.before[test.op[2]]):
        remove_op('mulr', test.op[0])
    if test.after[test.op[3]] != (test.before[test.op[1]] & test.op[2]):
        remove_op('bani', test.op[0])
    if test.after[test.op[3]] != (test.before[test.op[1]] & test.before[test.op[2]]):
        remove_op('banr', test.op[0])
    if test.after[test.op[3]] != (test.before[test.op[1]] | test.op[2]):
        remove_op('bori', test.op[0])
    if test.after[test.op[3]] != (test.before[test.op[1]] | test.before[test.op[2]]):
        remove_op('borr', test.op[0])
    if test.after[test.op[3]] != test.op[1]:
        remove_op('seti', test.op[0])
    if test.after[test.op[3]] != test.before[test.op[1]]:
        remove_op('setr', test.op[0])
    if (test.op[1] > test.before[test.op[2]] and test.after[test.op[3]] != 1) or (
            test.op[1] <= test.before[test.op[2]] and test.after[test.op[3]] != 0):
        remove_op('gtir', test.op[0])
    if (test.before[test.op[1]] > test.op[2] and test.after[test.op[3]] != 1) or (
            test.before[test.op[1]] <= test.op[2] and test.after[test.op[3]] != 0):
        remove_op('gtri', test.op[0])
    if (test.before[test.op[1]] > test.before[test.op[2]] and test.after[test.op[3]] != 1) or (
            test.before[test.op[1]] <= test.before[test.op[2]] and test.after[test.op[3]] != 0):
        remove_op('gtrr', test.op[0])
    if (test.op[1] == test.before[test.op[2]] and test.after[test.op[3]] != 1) or (
            test.op[1] != test.before[test.op[2]] and test.after[test.op[3]] != 0):
        remove_op('eqir', test.op[0])
    if (test.before[test.op[1]] == test.op[2] and test.after[test.op[3]] != 1) or (
            test.before[test.op[1]] != test.op[2] and test.after[test.op[3]] != 0):
        remove_op('eqri', test.op[0])
    if (test.before[test.op[1]] == test.before[test.op[2]] and test.after[test.op[3]] != 1) or (
            test.before[test.op[1]] != test.before[test.op[2]] and test.after[test.op[3]] != 0):
        remove_op('eqrr', test.op[0])

ready = []
while len(ready) < len(rops):
    for i in range(len(rops)):
        if i not in ready and len(ops[i]) == 1:
            ready.append(i)
            single_op = ops[i][0]
            for j in range(len(rops)):
                if j != i:
                    remove_op(single_op, j)
        continue

for num,v in ops.items():
    ops[num] = v[0]


instructions = []
with open('day16-input-2.txt') as raw_instructions:
    for line in raw_instructions:
        instructions.append(list(map(int, re.findall('\\d+', line))))

registers = [0, 0, 0, 0]
for instruction in instructions:
    print(instruction)
    operation = ops[instruction[0]]
    if (operation == "addi"):
        registers[instruction[3]] = registers[instruction[1]] + instruction[2]
    elif (operation == "addr"):
        registers[instruction[3]] = registers[instruction[1]] + registers[instruction[2]]
    elif (operation == "muli"):
        registers[instruction[3]] = registers[instruction[1]] * instruction[2]
    elif (operation == "mulr"):
        registers[instruction[3]] = registers[instruction[1]] * registers[instruction[2]]
    elif (operation == "bani"):
        registers[instruction[3]] = registers[instruction[1]] & instruction[2]
    elif (operation == "banr"):
        registers[instruction[3]] = registers[instruction[1]] & registers[instruction[2]]
    elif (operation == "bori"):
        registers[instruction[3]] = registers[instruction[1]] | instruction[2]
    elif (operation == "borr"):
        registers[instruction[3]] = registers[instruction[1]] | registers[instruction[2]]
    elif (operation == "seti"):
        registers[instruction[3]] = instruction[1]
    elif (operation == "setr"):
        registers[instruction[3]] = registers[instruction[1]]
    elif (operation == "gtri"):
        if registers[instruction[1]] > instruction[2]:
            registers[instruction[3]] = 1
        else:
            registers[instruction[3]] = 0
    elif (operation == "gtir"):
        if instruction[1] > registers[instruction[2]]:
            registers[instruction[3]] = 1
        else:
            registers[instruction[3]] = 0
    elif (operation == "gtrr"):
        if registers[instruction[1]] > registers[instruction[2]]:
            registers[instruction[3]] = 1
        else:
            registers[instruction[3]] = 0
    elif (operation == "eqri"):
        if registers[instruction[1]] == instruction[2]:
            registers[instruction[3]] = 1
        else:
            registers[instruction[3]] = 0
    elif (operation == "eqir"):
        if instruction[1] == registers[instruction[2]]:
            registers[instruction[3]] = 1
        else:
            registers[instruction[3]] = 0
    elif (operation == "eqrr"):
        if registers[instruction[1]] == registers[instruction[2]]:
            registers[instruction[3]] = 1
        else:
            registers[instruction[3]] = 0

print(registers[0])