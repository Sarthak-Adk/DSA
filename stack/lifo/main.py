# ==========================
# Stack Implementation
# ==========================

class Stack:
    def __init__(self):
        self.items = []

    # Push an element onto the stack
    def push(self, value):
        self.items.append(value)
        print(f"{value} pushed into stack")

    # Pop the top element
    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.items.pop()

    # Peek at the top element
    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    # Check if stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # Return stack size
    def size(self):
        return len(self.items)

    # Display stack
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack (Top -> Bottom):")
            for item in reversed(self.items):
                print(item)


# ==========================
# Example Usage
# ==========================

stack = Stack()

print("----- Push -----")
stack.push(10)
stack.push(20)
stack.push(30)

print("\n----- Display -----")
stack.display()

print("\n----- Peek -----")
print("Top Element:", stack.peek())

print("\n----- Pop -----")
print("Removed:", stack.pop())

print("\n----- Display After Pop -----")
stack.display()

print("\n----- Size -----")
print("Size:", stack.size())

print("\n----- Is Empty -----")
print(stack.is_empty())

# ==========================
# Reverse String Using Stack
# ==========================

def reverse_string(text):
    stack = []

    for ch in text:
        stack.append(ch)

    result = ""

    while stack:
        result += stack.pop()

    return result

print("\n----- Reverse String -----")
print(reverse_string("hello"))

# ==========================
# Valid Parentheses
# ==========================

def is_valid_parentheses(s):
    stack = []
    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack:
                return False
            if stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0

print("\n----- Valid Parentheses -----")
print(is_valid_parentheses("()[]{}"))
print(is_valid_parentheses("(]"))

# ==========================
# Next Greater Element
# ==========================

def next_greater(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):

        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(nums[i])

    return result

print("\n----- Next Greater Element -----")
nums = [2, 1, 3, 5, 4]
print("Input :", nums)
print("Output:", next_greater(nums))