'''
Remove K from List - Codesignal

Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Details: https://app.codesignal.com/interview-practice/task/gX7NXPBrYThXZuanm/description
'''
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
    # TODO improve the representation to show values from linked nodes
    def __repr__(self): 
        return repr(self.value)

def removeKFromList(l, k):
    current = l
    previous = None
    while current:
        if current.value == k:
            if previous:
                previous.next = current.next
            else:
                l = l.next
        else:
            previous = current
        current = current.next
    return l

# test
# l: [3, 1, 2, 3], k:3

a = ListNode(3)
a.next = ListNode(1)
a.next.next = ListNode(2)
a.next.next.next = ListNode(3)
k = 3

print(a)
print(removeKFromList(a,k))
