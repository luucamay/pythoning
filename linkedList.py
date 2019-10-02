class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

head = Node(8)
head.next = Node(12)
head.next.next = Node(8)
print head.data
print "holap"
