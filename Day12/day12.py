from dataclasses import dataclass
import operator


@dataclass
class Pot:
    index: int
    value: str

state = list()
next_state = list()
keys = dict()


def get_state_for_index(index: int):
    global state

    for pot in state:
        if pot.index == index:
            # print(f'Key for {index}: {pot.value}')
            return pot.value

    # print(f'pot not found for index {index}')
    return '.'


def build_key_for_index(index: int):
    key = ''
    for i in range(index-2, index+3):
        key = key + get_state_for_index(i)

    return key


def update_state_for_index(index):
    # build key
    print(f'Building key for index {index}')
    key = build_key_for_index(index)
    # get new value
    pot_state = keys.get(key, '.')
    print(f'Updating for key [{key}] to value {pot_state} for index {index}')
    global next_state

    # not found, add it
    next_state.append(Pot(index, pot_state))


def print_state():
    global state
    s = sorted(state, key=lambda x: x.index)
    p = '..'
    for pot in s:
        p = p+pot.value

    p = p+'..'
    print(p)


def get_start_index():
    global state
    state.sort(key=lambda x: x.index)
    for p in state:
        if p.value == '#':
            print(f'End Index {p.index}')
            return p.index

    return 0


def get_end_index():
    global state
    state.sort(key=lambda x: x.index, reverse=True)
    for p in state:
        if p.value == '#':
            print(f'End Index {p.index}')
            return p.index

    return len(state) - 1



with open('day12input.txt') as info:
    for line in info:
        if 'initial' in line:
            initial_state = line.split(':')[1].strip()
            for i in range(0, len(initial_state)):
                state.append(Pot(i, initial_state[i]))
                i = i+1

        elif line.strip():
            kv = line.split('=>')
            k = kv[0].strip()
            v = kv[1].strip()
            keys[k] = v
print(keys)
print(state)
print_state()

#change range for generations
for g in range(20):
    for i in range(get_start_index()-2, get_end_index() + 3):
        update_state_for_index(i)

    state.clear()
    for p in next_state:
        state.append(p)

    next_state.clear()
    print_state()

total = 0

for p in state:
    if p.value == '#':
        total = total + p.index

print(total)
