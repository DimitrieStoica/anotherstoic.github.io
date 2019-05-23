class Node:
    def __init__(self, value):
        self._left = None
        self._right = None
        self._value = value

def checkSubtree(tree, subtree):
    if tree is None:
        return False

    if subtree is None:
        return True

    if _checkSubtree(tree, subtree):
        return True

    return checkSubtree(tree._left, subtree) or checkSubtree(tree._right, subtree)

def _checkSubtree(root1, root2):

    if (root1 is None) and (root2 is None):
        return True

    if (root1 is None) or (root2 is None):
        return False

    #check if the value of the 2 roots is the same
    return ((root1._value == root2._value) 
            and _checkSubtree(root1._left, root2._left) 
            and _checkSubtree(root1._right, root2._right))

#tree
root1 = Node(1)
node11 = Node(2)
node12 = Node(3)
node13 = Node(4)
node14 = Node(5)

root1._left = node11
root1._right = node12
node11._left = node13
node11._right = node14

#subtree
root2 = Node(1)
node21 = Node(12)
node22 = Node(3)

root2._left = node21
root2._right = node22

print(checkSubtree(root1, root2))
