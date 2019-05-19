class Node:
    def __init__(self, value):
        self._value = value
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None

    def addFirst(self, newValue):
        newNode = Node(newValue)
        newNode._next = self._head
        self._head = newNode

    def addLast(self, newValue):
        newNode = Node(newValue)
        if not self._head:
            self._head = newNode
            return

        currentNode = self._head
        while currentNode._next:
            currentNode = currentNode._next
        currentNode._next = newNode

    def addAfter(self, prevNode, newValue):
        newNode = Node(newValue)

        newNode._next = prevNode._next
        prevNode._next = newNode

    def remove(self):
        if self._head == None:
            return None
        elif self._head._next == None:
            self._head = None
            return None
        else:
            currentNode = self._head
            while currentNode._next._next:
                currentNode = currentNode._next
            currentNode._next = None
	
    def printVal(self):
        currentNode = self._head
        while currentNode:
            print(currentNode._value)
            currentNode = currentNode._next

list1 = LinkedList()
list1._head = Node(1)
node2 = Node(2)
node3 = Node(3)

list1._head._next = node2
node2._next = node3

list1.addAfter(node2, 5)
list1.printVal()
