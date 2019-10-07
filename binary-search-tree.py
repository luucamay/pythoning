class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        pass

    def search(self, find_val):
        return False

    def print_tree(self):
        return self.inorder_print(self.root,"")[:-1]

    def inorder_print(self, currentNode, traversal):
        if currentNode:
            traversal = self.inorder_print(currentNode.left,traversal)
            traversal += (str(currentNode.value) + "-")
            traversal = self.inorder_print(currentNode.right,traversal)
        return traversal
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print tree.print_tree()

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)