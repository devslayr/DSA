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



# def evalute_postfix(expression):
#     s = []

#     for T in expression.split():
#         if T not in "+-*/":
#             s.append(float(T))
#         else:
#             operand1 = s.pop()
#             operand2 = s.pop()
#             if T == "+":
#                 result = operand2 + operand1
#             elif T == "-":
#                 result = operand2 - operand1
#             elif T == "*":
#                 result = operand2 * operand1
#             else:
#                 result = operand2 / operand1
#             s.append(result)
        
#     return s[-1]
    
# print(evalute_postfix("5 6 - 2 *"))