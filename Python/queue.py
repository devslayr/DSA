class ListQueue:
    def __init__(self):
        self._items = []
    def enQueue(self, item):
        self._items.append(item)
    def deQueue(self):
        return self._items.pop(0)
    def peek(self):
        return self._items[0]

class PointerQueue:
    def __init__(self):
        self._items = []
        self._front = 0

    def deQueue(self):
        item = self._items[self._front]
        self._front += 1
        return item
    
queue = ListQueue()

queue.enQueue(1)
print(queue.peek())

queue.enQueue(3)
print(queue.peek())

queue.deQueue()
print(queue.peek())


class PointerQueue:
    def __int__(self):
        self._items = []
        self._front = 0

    def deQueue(self):
        item = self._items[self._front]
        self._front += 1
        return item