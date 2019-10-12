'''
Yoy are given a root of a binary tree.
Find the level for the binary tree with the minimum sum, and return that value.

For instance, in the example below, the sums of the trees are 10, 2+8=10, and 4+1+2=7. So, the answer here should be 7.
        10
        /\
    2       8
    /\       \
   4  1       2
'''
class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def minimum_level_sum(root):
    if not root:
        return 0
    min_sum = root.val
    queue = [root]
    while queue:
        count = len(queue)
        sum_val = 0
        while count > 0:
            count -= 1
            aux = queue.pop(0)
            sum_val += aux.val
            if aux.left:
                queue.append(aux.left)
            if aux.right:
                queue.append(aux.right)
        min_sum = min(sum_val, min_sum)
    return min_sum

# Test Case
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print minimum_level_sum(node)
