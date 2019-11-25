'''
Successor - Cracking the coding interview
Chapter 4, problem #6

Write an algorithm to find the "next" node (i.e., in-order successor) of a given
node in a binary search tree. You may assume that each node has a link to its parent

Hints: #79, # 91
'''
class Node:
    def __init__(self, val, left=None, right=None, parent=None):
        self.key = val
        self.left =left
        self.right = right
        self.parent = parent
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        
        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
            return
            
        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)
        while(currentNode is not None):    
            if(key < currentNode.key):
                if(currentNode.left is None):
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if(currentNode.right is None):
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right
    def getNodeByKey(self, key):
        currentNode = self.root
        while(currentNode is not None):
            if(key == currentNode.key):
                return currentNode
                
            if(key < currentNode.key):
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
            
        return None

    def successor(self, current):
        if not current:
            return None
        # find succesor
        if current.right:
            successor = current.right
            while successor.left:
                successor = successor.left
            return successor
        else:
            ancestor = current.parent
            while ancestor and ancestor.key < current.key:
                ancestor = ancestor.parent
            return ancestor

# Test
# Create a Binary Search Tree
bst  = BinarySearchTree()
bst.insert(5)
bst.insert(2)
bst.insert(1)
bst.insert(8)
bst.insert(6)
bst.insert(19)
bst.insert(10)
bst.insert(22)
bst.insert(9)
bst.insert(12)
bst.insert(21)
bst.insert(25)

test = bst.getNodeByKey(2)
succ = bst.successor(test)
# Print the key of the successor node
if succ is not None:
    print ("\nInorder Successor of %d is %d " \
            %(test.key , succ.key))
else:
    print ("\nInorder Successor doesn't exist")
