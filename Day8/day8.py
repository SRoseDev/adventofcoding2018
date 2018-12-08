from dataclasses import dataclass
import sys
sys.setrecursionlimit(10000) # program hits the default recursion limit


licenseFile = []
metaTotal = 0

@dataclass
class Node:
    children: list
    metadata: list


def process_list():
    global metaTotal
    # read first two elements for child count and metadata count
    childCount = int(licenseFile.pop(0))
    print(f'Child Count {childCount}')
    metaCount = int(licenseFile.pop(0))
    print(f'Meta Count {metaCount}')
    n = Node(list(), list())
    for i in range(0, childCount):
        n.children.append(process_list())
    # get the metadata
    for i in range(0, metaCount):
        metaValue = licenseFile.pop(0)
        metaTotal = metaTotal + int(metaValue)
        n.metadata.append(metaValue)

    print(f'Node Created: {n}')
    return n

with open('day8input.txt') as info:
    licenseFile = info.read().split(' ')

node = process_list()

print(node)
print(metaTotal)