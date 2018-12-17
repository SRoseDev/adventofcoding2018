from dataclasses import dataclass


@dataclass
class Node:
    def __init__(self, data, index, p, n):
        self.data = data
        self.index = index
        self.p = p
        self.n = n

cycle_count = 286051

# n1 = Node(3, 1, None, None)
#
# n2 = Node(7, 2, n1, n1)
# n1.n = n2
# n1.p = n2
#
# end = n2
recipe_count = 2
recipe = list()
recipe.append(3)
recipe.append(7)

elf1 = 0
elf2 = 1

while recipe_count < 10+cycle_count:
    new_recipe = recipe[elf1] + recipe[elf2]
    for c in str(new_recipe):
        recipe_count = recipe_count + 1
        recipe.append(int(c))

    # move elves
    # elf1['index'] = (elf1['index'] + 1 + elf1['recipe']) % len(recipe)
    # elf1['recipe'] = recipe[elf1['index']]

    # elf2['index'] = (elf2['index'] + 1 + elf2['recipe']) % len(recipe)
    # elf2['recipe'] = recipe[elf2['index']]

    elf1 = (elf1 + 1 + recipe[elf1]) % recipe_count
    elf2 = (elf2 + 1 + recipe[elf2]) % recipe_count

result = ''
for i in range(cycle_count, cycle_count+10):
    result = result + str(recipe[i])

print(result)

