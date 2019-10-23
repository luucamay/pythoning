import sys

class Stack:
    def __init__(self):
        self.storage = []
        self.mins = []
    def push(self, value):
        if value < self.min_stack():
            self.mins.append(value)
        self.storage.append(value)
    def pop_stack(self):
        value = self.storage.pop()
        if value == self.min_stack():
            self.mins.pop()
        return value
    def min_stack(self):
        if self.storage:
            return self.mins[-1]
        return sys.maxsize
    def peek(self):
        return self.storage[-1]


# Test, create stack of objects
stack = Stack()
stack.push(4)
stack.push(2)
stack.push(3)
stack.push(1)
element = stack.pop_stack()
print element, stack.min_stack()
element = stack.pop_stack()
print element, stack.min_stack()
element = stack.pop_stack()
print element, stack.min_stack()
element = stack.pop_stack()
print element, stack.min_stack()
