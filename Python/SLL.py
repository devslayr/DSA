class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
        self.size += 1

    def delete(self, data):
        previous = None
        current = self.head
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                self.size -= 1
                return True
            previous = current
            current = current.next
        return False


SLL = SinglyLinkedList()

SLL.append(7)
print(SLL.head.data)

SLL.append(11)
print(SLL.head.next.data)

SLL.append(-1)
print(SLL.head.next.next.data)

print(SLL.delete(7))

print(SLL.size)