class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.peek())      # 30
print(s.pop())       # 30
print(s.peek())      # 20
print(s.size())      # 2