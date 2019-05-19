class Node:
    def __init__(self, value):
        self._left = None
        self._right = None
        self._value = value


class BST:
    def __init__(self):
        self._root = None

    def insert(self, data):
        if self._root:
            self._insert(data, self._root)
        else:
            self._root = Node(data)

    def _insert(self, data, currentNode):
        if data < currentNode._value:
            if not currentNode._left:
                currentNode._left = Node(data)
            else:
                self._insert(data, currentNode._left)
        elif data > currentNode._value:
            if not currentNode._right:
                currentNode._right = Node(data)
            else:
                self._insert(data, currentNode._right)
        else:
            print('Value is already present in BST')

    def printTree(self):
        if self._root is not None:
            self._printTree(self._root)

    def _printTree(self, currentNode):
        if currentNode is not None:
            self._printTree(currentNode._left)
            print(currentNode._value)
            self._printTree(currentNode._right)

    def inOrderTraversal(self):
        if self._root is not None:
            return self._inOrderTraversal(self._root)

    def _inOrderTraversal(self, currrentNode):
        res = []
        if currrentNode is not None:
            res = self._inOrderTraversal(currrentNode._left)
            res.append(currrentNode._value)
            res = res + self._inOrderTraversal(currrentNode._right)
        return res

    def height(self):
        if self._root is None:
            return 0
        else:
            return self._height(self._root, 0)

    def _height(self, currentNode, currentHeight):
        if currentNode is None:
            return currentHeight
        leftHeight = self._height(currentNode._left, currentHeight + 1)
        rightHeight = self._height(currentNode._right, currentHeight + 1)
        return max(leftHeight, rightHeight)

    def preOrderTraversal(self):
        if self._root is not None:
            return self._preOrderTraversal(self._root)

    def _preOrderTraversal(self, currrentNode):
        res = []
        if currrentNode is not None:
            res.append(currrentNode._value)
            res = res + self._inOrderTraversal(currrentNode._left)
            res = res + self._inOrderTraversal(currrentNode._right)
        return res

    def postOrderTraversal(self):
        if self._root is not None:
            return self._postOrderTraversal(self._root)

    def _postOrderTraversal(self, currentNode):
        res = []
        if currentNode is not None:
            res = self._postOrderTraversal(currentNode._left)
            res = res + self._postOrderTraversal(currentNode._right)
            res.append(currentNode._value)
        return res

    def search(self, value):
        if self._root is not None:
            return self._search(self._root, value)
        else:
            return False

    def _search(self, currentNode, value):
        if currentNode is not None:
            if value == currentNode._value:
                return True
            elif value < currentNode._value and currentNode._left is not None:
                return self._search(currentNode._left, value)
            elif value > currentNode._value and currentNode._right is not None:
                return self._search(currentNode._right, value)
            else:
                return False

bst = BST()
bst.insert(27)
bst.insert(14)
bst.insert(35)
bst.insert(10)
bst.insert(19)
bst.insert(19)
bst.insert(31)
bst.insert(42)

bst.printTree()
print("Height: " + str(bst.height()))

print(bst.search(19))
