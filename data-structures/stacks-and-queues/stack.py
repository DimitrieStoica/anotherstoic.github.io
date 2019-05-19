class Stack:
    def __init__(self):
        self._list = []

    def push(self, value):
        self._list.append(value)

    def pop(self):
        self._list.pop(-1)

    def peak(self):
        return self._list[-1]

stack = Stack()

stack.push(1)
stack.push(3)
stack.push(4)

stack.pop()

print(stack.peak())
