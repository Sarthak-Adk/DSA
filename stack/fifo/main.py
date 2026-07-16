# ==========================
# Queue Implementation (FIFO)
# ==========================

from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    # Enqueue (Insert)
    def enqueue(self, value):
        self.queue.append(value)
        print(f"{value} added to queue")

    # Dequeue (Remove)
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return None
        return self.queue.popleft()

    # Front Element
    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    # Rear Element
    def rear(self):
        if self.is_empty():
            return None
        return self.queue[-1]

    # Check Empty
    def is_empty(self):
        return len(self.queue) == 0

    # Queue Size
    def size(self):
        return len(self.queue)

    # Display Queue
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Front ->", list(self.queue), "<- Rear")


# ==========================
# Example Usage
# ==========================

q = Queue()

print("----- Enqueue -----")
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("\n----- Display -----")
q.display()

print("\n----- Front -----")
print(q.front())

print("\n----- Rear -----")
print(q.rear())

print("\n----- Dequeue -----")
print("Removed:", q.dequeue())

print("\n----- Display -----")
q.display()

print("\n----- Size -----")
print(q.size())

print("\n----- Is Empty -----")
print(q.is_empty())