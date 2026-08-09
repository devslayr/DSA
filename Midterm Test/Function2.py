# complexity =
# class ListQueue:
#     def __init__(self):
#         self._items = []
#     def enQueue(self, item):
#         self._items.append(item)
#     def deQueue(self):
#         return self._items.pop(0)
#     def peek(self):
#         return self._items[0]


# def process_tickets(ticket_queue, remaining_time):
#     queue = ListQueue()
#     for ticket in ticket_queue:
#         queue.enQueue(ticket)

#     lst = []

#     # print(queue.deQueue()[1])
#     # print(queue.deQueue())

#     while queue._items:
#         lst.append(queue.peek())
#         remaining_time = remaining_time - queue.deQueue()[1]
#         if remaining_time < queue.peek()[1]:
#             break

#     for i in lst:
#         ticket_queue.pop(ticket_queue.index(i))

#     return lst


# complexit = O(n)
# def process_tickets(ticket_queue, remaining_time):
#     lst = []
#     i = 0
#     while ticket_queue:
#         if remaining_time >= ticket_queue[0][1]:
#             lst.append(ticket_queue.pop(0))
#             remaining_time -= lst[i][1]
#             i += 1
#         else:
#             break

#     return lst

# complexity = O(n)

def process_tickets(ticket_queue, remaining_time):
    processed = []
    count = 0

    while count < len(ticket_queue) and remaining_time >= ticket_queue[count][1]:
        processed.append(ticket_queue[count])
        remaining_time -= ticket_queue[count][1]
        count += 1

    del ticket_queue[:count]

    return processed

# ticket_queue = [
#     (101, 5),
#     (102, 10),
#     (103, 15),
#     (104, 8)
# ]

ticket_queue = [
    (201, 12),
    (202, 6),
    (203, 4)
]


# print(process_tickets(ticket_queue, 20))
print(process_tickets(ticket_queue, 25))
print(ticket_queue)