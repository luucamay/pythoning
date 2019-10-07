class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def search(self, find_val):
        return False
        
    def insert_helper(self, current, new_val):
        if current:
            if current.value < new_val:
                if current.right:
                    self.insert_helper(current.right, new_val)
                else:
                    current.right = Node(new_val)
            else:
                if current.left:
                    self.insert_helper(current.left, new_val)
                else:
                    current.left = Node(new_val)
        
    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.inorder_print(self.root,"")[:-1]

    def inorder_print(self, currentNode, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
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