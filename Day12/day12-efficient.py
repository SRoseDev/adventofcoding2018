import operator


state = dict()
next_state = dict()
keys = dict()
key = '.....' # initial key state


def get_state_for_index(index: int):
    global state

    return state.get(index, '.')


def build_key_for_index(index: int):
    key = ''
    for i in range(index-2, index+3):
        key = key + get_state_for_index(i)

    return key


def update_key_for_index(index: int):
    global key
    # print(key[1:] + get_state_for_index(index + 2))
    return key[1:] + get_state_for_index(index + 2)


def update_state_for_index(index: int):
    # build key
    # print(f'Building key for index {index}')
    global key
    key = update_key_for_index(index)
    # get new value
    pot_state = keys.get(key, '.')
    # print(f'Updating for key [{key}] to value {pot_state} for index {index}')
    global next_state

    # not found, add it
    next_state[index] = pot_state


def print_state():
    global state
    s = sorted(state.items(), key=operator.itemgetter(0))
    state_str = ''
    for p in s:
        state_str = state_str + p[1]

    print(state_str)


def get_start_index():
    global state
    s = sorted(state.items(), key=operator.itemgetter(0))
    for p in s:
        if state[p[0]] == '#':
            # print(f'End Index {p.index}')
            return p[0]

    return 0


def get_end_index():
    global state
    s = sorted(state.items(), key=operator.itemgetter(0), reverse=True)
    for p in s:
        if state[p[0]] == '#':
            # print(f'End Index {p.index}')
            return p[0]

    return len(state) - 1



with open('day12input.txt') as info:
    for line in info:
        if 'initial' in line:
            initial_state = line.split(':')[1].strip()
            for i in range(0, len(initial_state)):
                state[i] = initial_state[i]

        elif line.strip():
            kv = line.split('=>')
            k = kv[0].strip()
            v = kv[1].strip()
            keys[k] = v

# print(keys)
# print(state)
print_state()
last_total = 0
last_variance = 0
total_repeat_count = 0
stopping_index = 0
#change range for generations
for g in range(2000):
    # print(g)
    key = '.....'
    for i in range(get_start_index()-2, get_end_index() + 3):
        update_state_for_index(i)

    state.clear()
    for p in next_state:
        state[p] = next_state[p]

    next_state.clear()

    total = 0

    for p in state:
        if state[p] == '#':
            total = total + p

    variance = total - last_total
    last_total = total
    print(f'{g} {total} {variance} {last_variance}')
    if last_variance == variance:
        total_repeat_count = total_repeat_count + 1
        if total_repeat_count > 4:
            stopping_index = g
            break

    last_variance = variance
    #print_state()

print(f'Stopped at {stopping_index} with total of {last_total}')

grand_total = last_total + ((50000000000 - stopping_index - 1) * last_variance)

print(grand_total)
