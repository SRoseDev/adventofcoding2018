from dataclasses import dataclass
import string


@dataclass
class Node:
    name: str
    required: list
    next: list


@dataclass
class Worker:
    name: str
    currentNode: str
    remainingTime: int


nodes = dict()
available = set()
visited = set()
workers = list()

# build worker list
workers.append(Worker('1', '', 0))
workers.append(Worker('2', '', 0))
workers.append(Worker('3', '', 0))
workers.append(Worker('4', '', 0))
workers.append(Worker('5', '', 0))


def have_visited_required(node: Node):
    for r in node.required:
        if r not in visited:
            return False

    return True


def assign_worker(node: Node):
    # check for available worker
    for worker in workers:
        if worker.remainingTime == 0:
            # worker is done, assign to this node
            available.remove(node.name)
            worker.currentNode = node.name
            worker.remainingTime = string.ascii_uppercase.index(node.name)+61 # add 1 for indexing and 60 for question
            print(f'Assigned {worker}')
            break


with open('day7input.txt') as info:
    for line in info:
        segments = line.split(' ')
        c = segments[1]
        r = segments[7]

        # set requirements
        n = nodes.get(c, Node(c, list(), list()))
        n.next.append(r)
        nodes[c] = n
        # set next
        m = nodes.get(r, Node(r, list(), list()))
        m.required.append(c)
        nodes[r] = m

for req in nodes:
    print(f'{req} {nodes[req]}')


# build available list to start
for req in nodes.keys():
    if len(nodes[req].required) == 0:
        available.add(req)

print(sorted(available))

# start at 0, walk
cur = sorted(available)[0]
visited.add(cur)
visit = cur
seconds = 0

while not len(visited) == len(nodes):
    # determine next node with all requirements met and assign to worker
    for a in sorted(available):
        if have_visited_required(nodes[a]):
            assign_worker(nodes[a])

    # do work
    seconds = seconds+1
    for worker in workers:
        if worker.remainingTime > 0:
            worker.remainingTime = worker.remainingTime - 1
            #check completion
            if worker.remainingTime == 0:
                # add completion
                visited.add(worker.currentNode)
                # add all available nodes
                for n in nodes[worker.currentNode].next:
                    available.add(n)

print(seconds)
