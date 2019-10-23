'''
Stack Min
How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
Hints:
#27 Only changes when a smaller element is added
#59 Keep track of extra data at each node?
#78 Consider having each node know the minimum of its "substack" (all the elements
beneath it, including itself). 
'''
# Solution using additional stack for min values
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
