class Node:
    def __init__(self, value):
        self._left = None
        self._right = None
        self._value = value

def checkBalance(root):
    if root is not None:
        return _checkBalance(root)

def _checkBalance(currentNode):
    if currentNode is None: 
        return 0
    else:

        #go deep into the left subtree
        leftTree = _checkBalance(currentNode._left)

        #go deep into the right subtree
        rightTree = _checkBalance(currentNode._right)

        if (leftTree is None) or (rightTree is None):
            return None

        #check balanced tree condition
        if abs(leftTree - rightTree) > 1:
            return None

        #return subtree height
        return max(leftTree, rightTree) + 1

root = Node(10)
node1 = Node(11)
node2 = Node(12)
node3 = Node(13)
node4 = Node(14)

root._left = node1
root._right = node2
node1._left = node3
node1._right = node4

print(checkBalance(root))
