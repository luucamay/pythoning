'''
Binary Tree Level Order Traversal
Leetcode # 102

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        queue = [root]
        result = []
        while queue:
            parents = queue
            queue = []
            level = []
            for p in parents:
                level.append(p.val)
                if p.left:
                    queue.append(p.left)
                if p.right:
                    queue.append(p.right)
            result.append(level)
        return result
