'''
List cousins
Given a binary tree and a given node value, return all of the node's cousins. 
Two nodes are considered cousins if they are on the same level of the tree with different parents. 
You can assume that all nodes will have their own unique value.

Example:
#     1
#    / \
#   2   3
#  / \   \
# 4   6   5
print list_cousins(root, 5)
# [4, 6]
'''
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_cousins(root, val):
    if val == None or root == None:
        return []
    queue = [root]
    parents = []
    node_found = False
    brother = None
    while queue:
        parents = queue
        queue = []
        for n in parents:
            if n.left and n.left != brother:
                if n.left.val == val:
                    node_found = True
                    brother = n.right
                else:
                    queue.append(n.left)
            if n.right and n.right != brother:
                if n.right.val == val:
                    node_found = True
                    brother = n.left
                else:
                    queue.append(n.right)
        if node_found:
            return [x.val for x in queue]
    return []

# Test case
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.left.left = Node(10)
root.left.left.right = Node(11)
root.left.right = Node(6)
root.left.right.right = Node(13)
root.right = Node(3)
root.right.right = Node(5)
root.right.right.left = Node(23)
root.right.right.right = Node(7)

print list_cousins(root, 5)
print list_cousins(root, 4)
print list_cousins(root, 10)
print list_cousins(root, 13)

