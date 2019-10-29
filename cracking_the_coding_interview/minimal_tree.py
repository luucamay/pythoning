'''
Minimal Tree (P. 120) Sol(P. 253)
Given a sorted (increasing order) array with unique integeer elements,
write an algorithm to create a binary search tree with minimal height.
Hints:
# 19: A minimal binary tree has the same nodes on the left and on the right.
# 73: Try recursion, can you divide in subproblems?
# 116: Imagina there is a function CreateMinimalTree that returns a minimal tree
My hints:
Return the root!
'''
# 1st approach
class Node:
    def __init__(self, val, left=None, right=None):
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

def min_heigh_bin_tree(sorted_arr):
    return helper(sorted_arr)

def helper (arr):
    size = len(arr)
    if size > 0:
        quotient = size // 2
        node = Node(arr[quotient])
        if quotient != 0: # this means there was only one element in the array
            node.left = helper(arr[:quotient])
            node.right = helper(arr[quotient+1:])
    return node

# Test case
sorted_array = [1, 2, 3, 4, 5, 6, 7]
print_level_order(min_heigh_bin_tree(sorted_array))