from collections import defaultdict
class Node():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
def most_freq_subtree_sum(root):
    dictionary = defaultdict(int)
    sum_helper(root, dictionary)
    return max(dictionary, key = dictionary.get)
def sum_helper(root, dictionary):
    node = root
    if not node:
        return 0
    total = node.val + sum_helper(node.left, dictionary) + sum_helper(node.right, dictionary)

    dictionary[total] += 1
    return total

# Test cases
root = Node(3, Node(1), Node(-3))
print(most_freq_subtree_sum(root))
