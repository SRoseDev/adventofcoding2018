from dataclasses import dataclass


@dataclass
class Node:
    name: str
    required: list
    next: list


def have_visited_required(node: Node, visited: set):
    for r in node.required:
        if r not in visited:
            return False

    return True


nodes = dict()
with open('day7input.txt') as info:
    for line in info:
        segments = line.split(' ')
        c = segments[1]
        r = segments[7]

        #set requirements
        n = nodes.get(c, Node(c, list(), list()))
        n.next.append(r)
        nodes[c] = n
        #set next
        m = nodes.get(r, Node(r, list(), list()))
        m.required.append(c)
        nodes[r] = m

for req in nodes:
    print(f'{req} {nodes[req]}')

available = set()
visited = set()

#build available list to start
for req in nodes.keys():
    if len(nodes[req].required) == 0:
        available.add(req)

print(sorted(available))

#start at 0, walk
cur = sorted(available)[0]
visited.add(cur)
visit = cur
#add all available nodes
for n in nodes[cur].next:
    available.add(n)

while not len(visited) == len(nodes):
    print(f'Current Node {cur}')
    available.remove(cur)
    #add all available nodes
    for n in nodes[cur].next:
        available.add(n)

    #determine next node with all requirements met
    for a in sorted(available):
        if have_visited_required(nodes[a], visited):
            print(f'Moving to {a}')
            cur = a
            visited.add(a)
            visit = visit + a
            break

print(visit)
