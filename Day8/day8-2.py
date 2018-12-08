from dataclasses import dataclass
import sys
sys.setrecursionlimit(10000) # program hits the default recursion limit


licenseFile = []

@dataclass
class Node:
    children: list
    metadata: list


def process_list():
    # read first two elements for child count and metadata count
    childCount = licenseFile.pop(0)
    print(f'Child Count {childCount}')
    metaCount = licenseFile.pop(0)
    print(f'Meta Count {metaCount}')
    n = Node(list(), list())
    for i in range(0, childCount):
        n.children.append(process_list())
    # get the metadata
    for i in range(0, metaCount):
        metaValue = licenseFile.pop(0)
        n.metadata.append(metaValue)

    print(f'Node Created: {n}')
    return n


def get_node_value(n: Node):
    metaTotal = 0
    if len(n.children) == 0:
        # return sum of metadata
        for m in n.metadata:
            metaTotal = metaTotal + m

    else:
        for m in n.metadata:
            index = m - 1 # arrays start at 0!
            if index < len(n.children):
                metaTotal = metaTotal + get_node_value(n.children[index])

    return metaTotal

with open('day8input.txt') as info:
    lf = info.read().split(' ')
    for e in lf:
        licenseFile.append(int(e))

node = process_list()

print(node)
print(get_node_value(node))