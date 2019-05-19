class Node:
    def __init__(self, value):
        self._left = None
        self._right = None
        self._value = value

def levelOrderTraversal(root):
    if root is not None:
        levelList, queue = [], [root]

        while queue:
            currentLayer = []
            for i in range(len(queue)):
                currentNode = queue.pop(0)

                if currentNode is not None:
                    currentLayer.append(currentNode)

                    # process left side
                    if (currentNode._left is not None):
                        queue.append(currentNode._left)

                    # process right side
                    if (currentNode._right is not None):
                        queue.append(currentNode._right)

            levelList += currentLayer
        return levelList

def printTreeLevel(root, level):
    if root is not None:
        return _printTreeLevel(root, level)

def _printTreeLevel(currentNode, level):
    res = []
    if currentNode is not None:
        if level == 1:
            res.append(currentNode._value)
        elif level > 1:
            res = printTreeLevel(currentNode._left, level - 1)
            res = res + printTreeLevel(currentNode._right, level - 1)
    return res

root = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)
node5 = Node(6)

root._left = node1
root._right = node2
node1._left = node3
node1._right = node4
node4._right = node5

levelOrderList = levelOrderTraversal(root)

print(printTreeLevel(root, 2))
