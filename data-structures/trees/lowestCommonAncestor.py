class Node:
    def __init__(self, value):
        self._left = None
        self._right = None
        self._value = value

def lowestCommonAncestor(root, xNode, yNode):
    if root is not None:
        return _lowestCommonAncestor(root, xNode, yNode)
    else:
        return None

def _lowestCommonAncestor(currentNode, xNode, yNode):
    if currentNode is not None:
        if (currentNode._value == xNode._value) or (currentNode._value == yNode._value):
            return currentNode

        leftTree = _lowestCommonAncestor(currentNode._left, xNode, yNode)
        rightTree = _lowestCommonAncestor(currentNode._right, xNode, yNode)

        # I can reach 
        if leftTree is None:
            return rightTree

        if rightTree is None:
            return leftTree

        return currentNode

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

commonNode = lowestCommonAncestor(root, node3, node5)
print(commonNode._value)
