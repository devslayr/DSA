class Queue:
    def __init__(self):
        self.capacity = 100                 # fixed maximum size
        self.items = [None] * self.capacity # pre-allocated slots
        self.size = 0                       # how many slots are used
        self.front = 0                      # index of first element
        self.rear = 0                       # index of NEXT free slot

    def enqueue(self, item):                #
        if self.size < self.capacity:       # only if there's room
            self.items[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            self.size += 1

    def dequeue(self):
        if self.size > 0:
            item = self.items[self.front]
            self.front =  (self.front + 1) % self.capacity
            self.size -= 1
            return item
        return None

class Event:
    def __init__(self, arrival, duration):
        self.arrival = arrival
        self.duration = duration

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(Event(0, 5))
    queue.enqueue(Event(3, 3))
    queue.enqueue(Event(4, 4))
    queue.enqueue(Event(100, 4))

    n = queue.size
    next_available_time = 0
    total_waiting_time = 0
    max_waiting_time = 0

    while queue.size > 0:
        evt = queue.dequeue()
        next_available_time = max(next_available_time, evt.arrival)
        waiting_time = next_available_time - evt.arrival
        max_waiting_time = max(max_waiting_time, waiting_time)
        total_waiting_time += waiting_time
        next_available_time += evt.duration

    print(f"Max waiting time {max_waiting_time}")
    print(f"Total waiting time {total_waiting_time}")
    print(f"Average waiting time {total_waiting_time / n}")