'''
Remove duplicates from an unsorted linked list. (P. 105)
Follow up: How would you solve this problem if a temporary buffer is not allowed?
Hints: Use a hash table. Use two pointers where second searchs ahead of the first one.
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print node.data,
            node = node.next
        print ''

    def remove_duplicates(self):
        no_dups = []
        node = self
        previous = None
        while node != None:
            if node.data in no_dups:
                previous.next = node.next
            else:
                no_dups.append(node.data)
                previous = node
            node = node.next
    # Using a set
    def remove_dups(self):
        node = self
        previous = None
        my_set = set()
        while node:
            if node.data in my_set:
                previous.next = node.next
            else:
                my_set.add(node.data)
                previous = node
            node = node.next

# Test
head = Node(8)
head.next = Node(12)
head.next.next = Node(13)
head.next.next.next = Node (8)
head.next.next.next.next = Node(7)
head.next.next.next.next.next = Node (13)
head.next.next.next.next.next.next = Node (13)
head.next.next.next.next.next.next.next = Node (13)
head.next.next.next.next.next.next.next.next = Node (11)

head.traverse()
head.remove_dups()
head.traverse()
