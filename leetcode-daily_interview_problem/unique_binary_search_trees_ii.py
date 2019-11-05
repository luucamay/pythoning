'''
Unique binary search trees II

Leetcode #95
'''
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        result = str(self.val)
        if self.left:
            result = result + str(self.left)
        if self.right:
            result = result + str(self.right)
        return result

def generate_bst(n):
    return generate(1, n)

def generate(first, last):
    if first > last:
        return [None]

    trees = []
    for root in range(first, last + 1):
        lefts = generate(first, root - 1)
        rights = generate(root + 1, last)
        for left in lefts:
            for right in rights:
                node = Node(root)
                node.left = left
                node.right = right
                trees.append(node)
    return trees

# Test cases
# 123
# 132
# 213
# 312
# 321
new_bsts =  generate_bst(5)
for tree in new_bsts:
    print tree
