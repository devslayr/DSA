class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_loop(head):
    if head is None:
        return
    slow = head
    fast = head
    loop_found = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop_found = True
            break
    if not loop_found:
        return

    loop_lengeth = 1
    current = fast.next
    while current != fast:
        loop_lengeth += 1
        current = current.next

    fast = head
    for _ in range(loop_lengeth):
        fast = fast.next

    slow = head 
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    fast.next = None


if __name__ == "__main__":
    # list = LinkedList()
    # list.append(1)
    # list.append(2)
    # list.append(3)
    # list.print_list()

    # node = list.search(2)
    # print(node.data)
    # list.insert_after(node, 4)
    # list.print_list()
    # list.delete(1)
    # list.print_list()

    head = Node(1)
    current = head
    for i in range(2, 11):
        current.next = Node(i)
        current = current.next
    current.next = head.next.next.next # create a loop
    # print(head.data)

    # 2. before removing loop, let print the list 15 times, it will print 1 to 10,
    # and then print 4 to 10 again, and then print 4 to 10 again
    print("Before removing loop:")
    current = head
    for _ in range(15):
        print(current.data)
        current = current.next
        if not current:
            break

    # 3. REMOVE the loop
    print("\nAfter removing loop:")
    remove_loop(head)

    # after removing loop, let print the list 20 times, it will print 1 to 10 once and then stop
    current = head
    for _ in range(15):
        print(current.data)
        current = current.next
        if not current:
            break
