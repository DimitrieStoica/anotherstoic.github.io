class Node:
    def __init__(self, value):
        self._value = value
        self._next = None

node1 = Node(1)
node2 = Node(2)

node1._next = node2
