class Node:
    def __init__(self, value):
        self._left = None
        self._right = None
        self._value = value

def populateNodeToParent(root):
    res = {}
    if root is not None:
        return _populateNodeToParent(res, root, None)

def _populateNodeToParent(res, currentNode, parent):
    if currentNode is not None:
        res.update({currentNode: parent})
        _populateNodeToParent(res, currentNode._left, currentNode)
        _populateNodeToParent(res, currentNode._right, currentNode)
    
    return res
        
def distance(root, startNode, distance):
    seen, queue = set(), [startNode]
    seen.add(startNode)
    currentLayer = 0

    nodeToParentDict = populateNodeToParent(root)

    while queue:
        if currentLayer == distance:
            return queue

        for i in range(len(queue)):
            currentNode = queue.pop(0)

            if currentNode is not None:

                # add left node
                if (currentNode._left is not None) and (currentNode._left not in seen):
                    queue.append(currentNode._left)
                    seen.add(currentNode._left)

                # add right node
                if (currentNode._right is not None) and (currentNode._right not in seen):
                    queue.append(currentNode._right)
                    seen.add(currentNode._right)

                # add parent node
                parrentOfCurrentNode = nodeToParentDict.get(currentNode)
                if (parrentOfCurrentNode is not None) and (parrentOfCurrentNode not in seen):
                    queue.append(parrentOfCurrentNode)
                    seen.add(parrentOfCurrentNode)

        currentLayer += 1

root = Node(10)
node1 = Node(11)
node2 = Node(12)
node3 = Node(13)
node4 = Node(14)
node5 = Node(15)

root._left = node1
root._right = node2
node1._left = node3
node1._right = node4
node4._right = node5

nodes = distance(root, node1, 1)
for i in nodes:
    if i is not None:
        print(i._value)
