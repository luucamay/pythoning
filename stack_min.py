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
# Solution modifiying the Node
import sys
class NodeWithMin:
    def __init__(self, v, mini):
        self.value = v
        self.min = mini

class Stack:
    def __init__(self):
        self.storage = []
    def push(self, value):
        new_min = min(value, self.min_stack())
        new_element = NodeWithMin(value, new_min)
        self.storage.append(new_element)
    def pop_stack(self):
        return self.storage.pop()
    def min_stack(self):
        if self.storage:
            return self.peek().min
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
print element.min, element.value
element = stack.pop_stack()
print element.min, element.value
element = stack.pop_stack()
print element.min, element.value
element = stack.pop_stack()
print element.min, element.value
