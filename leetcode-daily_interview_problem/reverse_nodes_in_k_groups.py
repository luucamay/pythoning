'''
Reverse nodes in k groups - CodeSignal

Given a linked list and an integer K, the task is to reverse every K nodes of the given linked list.
'''
# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x, next=None):
        self.value = x
        self.next = next
def reverseNodesInKGroups(l, k):
    if k <= 1 or not l or not l.next:
        return l
     
    prev = None
    curr = l 
    temp = None
    tail = None
    newHead = None
    join = None
    t = 0
  
    # Traverse till the end of the linked list  
    while (curr) :  
        t = k  
        join = curr  
        prev = None
        
        # Reverse group of k nodes of the linked list  
        while (curr and t > 0): 
            temp = curr.next
            curr.next = prev 
            prev = curr 
            curr = temp 
            t = t - 1
  
        # Sets the new head of the input list  
        if (newHead == None):  
            newHead = prev  
  
        # Tail pointer keeps track of the last node  
        # of the k-reversed linked list. We join the  
        # tail poer with the head of the next  
        # k-reversed linked list's head  
        if (tail != None):  
            tail.next = prev  
  
        # The tail is then updated to the last node  
        # of the next k-reverse linked list  
        tail = join  
      
    # newHead is new head of the input list */ 
    return newHead

# Test
l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print l
k = 2
print reverseNodesInKGroups(l,k)