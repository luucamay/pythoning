'''
Rotate Linked List
Daily Interview Problem - Leetcode #61

Given a linked list and a number k, rotate the linked list by k places.

My error in the first solution is not considering k bigger than size of my list.
right_rotate_list considers the case where k is bigger to the size of my list.
'''
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    current = self
    ret = ''
    while current:
      ret += str(current.value)
      current = current.next
    return ret

def rotate_list(list, k):
    if k == 0 or list == None:
        return list
    current = list
    index = 1
    while current.next:
        if index == k:
            new_head = current.next
            tail = current
        index += 1
        current = current.next
    
    tail.next = None
    current.next = list
    return new_head

def right_rotate_list(head, k):
    if k == 0 or head == None:
            return head
    current = head
    # get the tail
    size = 1
    while current.next:
        current = current.next    
        size += 1
    tail = current
    current = head
    k = k % size
    # looking for the new head
    for i in range(1, size - k):
        current = current.next
    tail.next = head
    new_head = current.next
    current.next = None
    return new_head

# Order is 1, 2, 3, 4
llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))

# Order should now be 3, 4, 1, 2
print(rotate_list(llist, 2))
# 3412

nlist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(right_rotate_list(nlist, 2))