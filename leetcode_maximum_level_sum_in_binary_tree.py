'''
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = collections.deque()
        q.append(root)
        q.append(None)
        node = None
        level=maxlevel=1
        curSum=maxSum=0
        while q:
            node = q.popleft()
            if node == None:
                if curSum > maxSum:
                    maxSum = curSum
                    maxlevel = level
                curSum = 0 
                if q:
                    q.append(None)
                    level += 1
            else:
                curSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return maxlevel
