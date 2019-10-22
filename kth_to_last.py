'''
Find the kth to last element of a singly linked list.
Hints:
8: What if path has to start at root
25: If you don't know the linked list size can you compute it
41: Recursively, find the k -1
67: Find usefull to return multiple values
126: Can you do it iteratively?
'''
class Node:
    def __init__(self, value, nextNode = None):
        self.val = value
        self.next = nextNode
# Itereative solution
def kth_to_last(root, k):
    p1 = p2 = root
    # Move k nodes into the list
    for i in range(k):
        if not p1:
            return None
        p1 = p1.next
    # Move p1 until the end of the list
    while p1:
        p1 = p1.next
        p2 = p2.next
    return p2.val

# Test
node = Node(8)
node.next = Node(2)
node.next.next = Node(3)
node.next.next.next = Node(4)
print kth_to_last(node, 3)
