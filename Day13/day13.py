from dataclasses import dataclass
import functools


@dataclass
class Cart:
    x: int
    y: int
    direction: str
    last_turn: str

    def __cmp__(self, other):
        if not self.y == other.y:
            return self.y - other.y
        else:
            return self.x - other.x

turn_right = {
    '^': '>',
    '>': 'v',
    'v': '<',
    '<': '^'
}

turn_left = {
    '^': '<',
    '>': '^',
    'v': '>',
    '<': 'v'
}

next_turn = {
    '>': '<',
    '<': '^',
    '^': '>'
}

track = dict()
carts = list()
hadCrash = False


def compare_carts(item1, item2):
    if not item1.y == item2.y:
        return item1.y - item2.y
    else:
        return item1.x - item2.x


def get_next_track(cart: Cart):
    if cart.direction == '^':
        return track[f'{cart.x},{cart.y - 1}']
    elif cart.direction == '>':
        return track[f'{cart.x + 1},{cart.y}']
    elif cart.direction == 'v':
        return track[f'{cart.x},{cart.y + 1}']
    else:
        return track[f'{cart.x - 1},{cart.y}']


def move_cart(cart: Cart, next_track: str):
    if next_track == '|':
        if cart.direction == '^':
            cart.y = cart.y - 1
        else:
            cart.y = cart.y + 1

    elif next_track == '-':
        if cart.direction == '<':
            cart.x = cart.x - 1
        else:
            cart.x = cart.x + 1

    elif next_track == '\\':
        if cart.direction == 'v':
            cart.y = cart.y + 1
            cart.direction = turn_left[cart.direction]
        elif cart.direction == '>':
            cart.x = cart.x + 1
            cart.direction = turn_right[cart.direction]
        elif cart.direction == '^':
            cart.y = cart.y - 1
            cart.direction = turn_left[cart.direction]
        else:
            cart.x = cart.x - 1
            cart.direction = turn_right[cart.direction]

    elif next_track == '/':
        if cart.direction == '<':
            cart.x = cart.x - 1
            cart.direction = turn_left[cart.direction]
        elif cart.direction == '>':
            cart.x = cart.x + 1
            cart.direction = turn_left[cart.direction]
        elif cart.direction == '^':
            cart.y = cart.y - 1
            cart.direction = turn_right[cart.direction]
        else:
            cart.y = cart.y + 1
            cart.direction = turn_right[cart.direction]

    else:
        # intersection
        turn = next_turn[cart.last_turn]

        if cart.direction == '^':
            cart.y = cart.y - 1

        elif cart.direction == '>':
            cart.x = cart.x + 1

        elif cart.direction == 'v':
            cart.y = cart.y + 1

        else:
            cart.x = cart.x - 1

        if turn == '<':
            cart.direction = turn_left[cart.direction]
        elif turn == '>':
            cart.direction = turn_right[cart.direction]

        cart.last_turn = turn


def move_carts():
    global hadCrash
    for cart in carts:
        # move cart one space in current direction
        next_track = get_next_track(cart)
        move_cart(cart, next_track)
        locs = list()
        for cart in carts:
            loc = f'{cart.x},{cart.y}'
            if loc in locs:
                hadCrash = True
                print(loc)
                break
            locs.append(loc)


with open ('day13input.txt') as info:
    l = 0
    for line in info:
        x = 0
        for c in line:
            key = f'{x},{l}'
            if c == '^':
                cart = Cart(x, l, c, '>')
                carts.append(cart)
                track[key] = '|'

            elif c == '>':
                cart = Cart(x, l, c, '>')
                carts.append(cart)
                track[key] = '-'

            elif c == 'v':
                cart = Cart(x, l, c, '>')
                carts.append(cart)
                track[key] = '|'

            elif c == '<':
                cart = Cart(x, l, c, '>')
                carts.append(cart)
                track[key] = '-'

            elif c:
                track[key] = c

            x = x+1

        l = l+1

print(carts)

while not hadCrash:
#for m in range(20):
    move_carts()
    # sort carts
    carts = sorted(carts, key=functools.cmp_to_key(compare_carts))
    print(carts)
    # check all for collision



