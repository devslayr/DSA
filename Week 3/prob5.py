class Stack:
    def __init__(self):
        self.size = 0
        self._items = []

    def push(self, item):
        self._items.append(item)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self._items.pop()
        return None

    def peek(self):
        if self.size > 0:
            return self._items[-1]
        return None
    
    def is_empty(self):
        return self.size == 0

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    print(stack.peek())