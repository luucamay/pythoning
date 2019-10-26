class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root,"")[:-1]

    def preorder_search(self, currentNode, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if currentNode:
            if currentNode.value == find_val:
                return True
            else:
                return self.preorder_search(currentNode.left,find_val) or self.preorder_search(currentNode.right,find_val)
        return False

    def preorder_print(self, currentNode, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if currentNode:
            traversal += (str(currentNode.value) + "-")
            traversal = self.preorder_print(currentNode.left,traversal)
            traversal = self.preorder_print(currentNode.right,traversal)
        return traversal


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()
