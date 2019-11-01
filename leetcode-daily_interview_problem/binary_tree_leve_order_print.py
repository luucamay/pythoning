'''
Daily Interview Problem
Print in level order a binary tree
'''
class Node:
    def __init__ (self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def print_level_order(root):
    queue = []
    queue.append(root)
    while queue:
        root = queue.pop(0)
        print root.val,
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
