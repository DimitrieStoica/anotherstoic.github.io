class Queue:
    def __init__(self):
        self._list = []

    def add(self, value):
        self._list.insert(0, value)

    def remove(self):
        self._list.pop(0)

    def peek(self):
        return self._list[-1]

queue = Queue()
queue.add(1)
queue.add(2)

print(queue.peek())
