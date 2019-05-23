class Node:
    def __init__(self, value):
        self._left = None
        self._right = None
        self._value = value

def verticalSum(root):
    res = {}
    if root is not None:
        return _verticalSum(res, root, 0)

def _verticalSum(res, currentNode, distance):
    if currentNode is not None:
        currentSum = res.get(distance) or 0
        res.update({distance: currentNode._value + currentSum})
        _verticalSum(res, currentNode._left, distance - 1)
        _verticalSum(res, currentNode._right, distance + 1)

    return res

root = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)

root._left = node1
root._right = node2
node1._left = node3
node1._right = node4

print(verticalSum(root))
