# The following program is the solution to the Binary Search Tree Practice quiz of the Data Structures & Algorithms class by Grow with Google/Udacity

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)
        self.found = False

    def insert(self, root, new_val):
        if root is None:
            return
        if new_val < root.value and root.left is None:
            root.left = Node(new_val)
            return
        elif new_val > root.value and root.right is None:
            root.right = Node(new_val)
            return
        self.insert(root.left,new_val)
        self.insert(root.right,new_val)

    def search(self, find_val):
        self.preorder_search(self.root,find_val)
        answer = self.found
        self.found = False
        return answer
    
    def preorder_search(self, root, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if root == None:
            return
        if root.value == find_val:
            self.found = True
        self.preorder_search(root.left,find_val)
        self.preorder_search(root.right,find_val)
        
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(tree.root,2)
tree.insert(tree.root,1)
tree.insert(tree.root,3)
tree.insert(tree.root,5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
