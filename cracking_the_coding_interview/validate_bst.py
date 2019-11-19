'''
Validate BST
Chapter 4, Exercise #4
'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def is_bst(root, min=float('-inf'), max=float('inf')):
    if not root:
        return True
    if root.val <= min or root.val >= max:
        return False
    return is_bst(root.left, min, root.val) and is_bst(root.right, root.val, max)

# Test
root = TreeNode(5, TreeNode(2, TreeNode(1), TreeNode(4)), TreeNode(8, TreeNode(6)))
print is_bst(root)
