class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        # empty list -> new node becomes head and tail
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            # attach to the end and update tail
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = None
            self.tail = new_node

        self.size += 1
        return new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.size -=1
                return True

            current = current.next

        return False
        
DLL = DoublyLinkedList()

DLL.append(7)
print(DLL.head.data)
print(DLL.head.prev)

DLL.append(11)
print(DLL.head.next.data)
print(DLL.tail.prev.data)

DLL.append(-1)
print(DLL.head.next.next.data)
print(DLL.tail.prev.data)
print(DLL.tail.prev.prev.data)
print(DLL.tail.next)

print(DLL.delete(-1))