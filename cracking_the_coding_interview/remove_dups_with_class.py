'''
Remove Dups - Cracking the coding interview
Chapter 2, Problem #1

Write code to remove duplicates from an unsorted linked list.
Follow up:
How would you solve this problem if a temporary buffer is not allowed

Hints
#9: Have you tried a hash table?
#40: Without extra space, you'll need O(n^2) time. Try using two pointers, where the second one searches ahead of the first one.
'''

# This way of list construction comes from
# https://dbader.org/blog/python-linked-list

class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __repr__(self):
        return repr(self.value)

class LinkedList:
    def __init__(self, head=None):
        self.head = head
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current))
            current = current.next
        return '[' + ','.join(nodes) + ']'
    def preprend(self, value):
        self.head = ListNode(value, self.head)
    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(value)
    def remove(self, key):
        current = self.head
        previous = None
        while current and current.value != key:
            previous = current
            current = current.next
        if previous is None:
            self.head = current.next
        elif current:
            previous.next = current.next
            current.next = None
    def remove_dups(self):
        current = self.head
        previous = None
        values = set()
        while current:
            if current.value in values:
                previous.next = current.next
            else:
                values.add(current.value)
                previous = current
            current = current.next

# Test
lst = LinkedList()
lst.append(8)
lst.append(12)
lst.append(13)
lst.append(8)
lst.append(7)
lst.append(13)
lst.append(13)
lst.append(13)
lst.append(11)
print(lst)
lst.remove_dups()
print(lst)
