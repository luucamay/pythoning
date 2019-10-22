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
head.remove_duplicates()
head.traverse()
