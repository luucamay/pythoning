'''
Check Balanced
Chapter 4 - Exercise #4 - Cracking the Coding Interview

Implement a function to check if a binary tree is balanaced.
For the purposes of this question, a balanced tree is defined
to be atree such that heights of the two subtree of any node never differ by more than 1.
Hints: #21, #33 #49 #105 #124
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        answer = str(self.value)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer
def is_balanced(root):
    return check_height(root) != float('-inf')
def check_height(root):
    if not root:
        return -1
    left_height = check_height(root.left)
    if  left_height == float('-inf'):
        return left_height
    right_height = check_height(root.right)
    if right_height == float('-inf'):
        return right_height
    diff = abs(left_height - right_height)
    if diff > 1:
        return float('-inf')
    else:
        return max(left_height, right_height) + 1

root = TreeNode(2)
a = TreeNode(1)
b = TreeNode(3)
c = TreeNode(4)
d = TreeNode(5)
e = TreeNode(6)
f = TreeNode(7)
g = TreeNode(8)
h = TreeNode(9)
root.left = a
root.right = b
a.left = c
a.right = d
b.right = e
c.left = f
c.right = g
f.left = h
print is_balanced(root)