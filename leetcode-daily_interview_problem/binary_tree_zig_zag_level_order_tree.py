'''
Binary Tree Zigzag Level Order Traversal
Leetcode #103

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root: return result
        
        left_to_right = True
        queue = deque()
        queue.append(root)
        while queue:
            size = len(queue)
            row = [0]*size
            for i in range(size):
                node = queue.popleft()
                
                index = i
                if not left_to_right:
                    index = size - 1 - i
                row[index] = node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            left_to_right = not left_to_right
            result.append(row)
        return result

n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n2 = TreeNode(2, n4, n5)
n3 = TreeNode(3, n6, n7)
n1 = TreeNode(1, n2, n3)
s = Solution()
print (s.zigzagLevelOrder(n1)) 