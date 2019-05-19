class Node:
    def __init__(self, value):
        self._left = None
        self._right = None
        self._value = value

def dfs(root, startNode, endNode):
    stack = [(startNode, [startNode])]
    seen = set()
    seen.add(startNode)

    populateNodeToParentDict = populateNodeToParent(root)

    while stack:
        for i in range(len(stack)):
            (currentNode, path) = stack.pop()

            if currentNode == endNode:
                return path

            if currentNode is not None:
                if (currentNode._left is not None) and (currentNode._left not in seen):
                    seen.add(currentNode._left)
                    stack.append((currentNode._left, path + [currentNode._left]))

                if (currentNode._right is not None) and (currentNode._right not in seen):
                    seen.add(currentNode._right)
                    stack.append((currentNode._right, path + [currentNode._right]))

                parrentOfCurrentNode = populateNodeToParentDict.get(currentNode)
                if (parrentOfCurrentNode is not None) and (parrentOfCurrentNode not in seen):
                    seen.add(parrentOfCurrentNode)
                    stack.append((parrentOfCurrentNode, path + [parrentOfCurrentNode]))

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

path = dfs(root, root, node4)

for i in path:
    print(i._value)
