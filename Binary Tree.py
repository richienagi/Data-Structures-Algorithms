# The following program is the solution to the Binary Tree Practice quiz of the Data Structures & Algorithms class by Grow with Google/Udacity

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        self.found = False
        self.list = []

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        self.preorder_search(self.root,find_val)
        answer = self.found
        self.found = False
        return answer
        
    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        ans = ''
        self.preorder(self.root)
        del self.list[len(self.list)-1]
        for i in range(0,len(self.list)):
            ans = ans + str(self.list[i])
        print(ans)

    def preorder_search(self, root, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if root == None:
            return
        if root.value == find_val:
            self.found = True
        self.preorder_search(root.left,find_val)
        self.preorder_search(root.right,find_val)
        
    def preorder(self, root):
        """Helper method - use this to create a 
        recursive print solution."""
        if root == None:
            return
        self.list.append(root.value)
        self.list.append('-')
        #print(root.value,'',end = '')
        self.preorder(root.left)
        self.preorder(root.right)


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
tree.print_tree()
