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
    text = input("Enter an expression that contains parentheses: ")
    stack = Stack()
    balanced = True
    for char in text:
        print(char)
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                balanced = False
                break
            top = stack.pop()
            if (char == ')' and top != '(') or \
               (char == ']' and top != '[') or \
               (char == '}' and top != '{'):
                balanced = False
                break

    if not stack.is_empty():
        balanced = False

    if balanced:
        print("The parentheses are balanced.")
    else:
        print("The parentheses are not balanced.")