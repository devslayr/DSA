class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        new_node.next = self.head
        self.size += 1
        return new_node

    def delete(self, prev_node, delete_node):
        if self.size == 0:
            return False
        if delete_node == self.head:
            if self.size == 1:
                self.head = None
                self.tail = None
            else:
                self.head = delete_node.next
                self.tail.next = self.head
            self.size -= 1
            return True
        if delete_node == self.tail:
            prev_node.next = self.head
            self.tail = prev_node
            self.size -= 1
            return True
        prev_node.next = delete_node.next
        self.size -= 1
        return True

if __name__ == "__main__":
    circular_list = CircularLinkedList()
    for i in range(1, 42):
        circular_list.append(i)
    current = circular_list.head
    # print(current.next.data)
    # print(current.next.next.data)
    # print(circular_list.tail.data)
    # print(circular_list.tail.next.data)

    while circular_list.size > 1:
        current = current.next
        print(f"Eliminate: {current.next.data}")
        circular_list.delete(current, current.next)
        current = current.next
    print("The last one is:", circular_list.head.data)
