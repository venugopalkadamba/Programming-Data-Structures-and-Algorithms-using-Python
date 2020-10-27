# Implementation of Binary Search Tree

class BinarySearchTree:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinarySearchTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinarySearchTree(data)
                else:
                    self.right.insert(data)
    
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data, end = ' ')
        if self.right:
            self.right.inorder_traversal()
    
    def preorder_traversal(self):
        print(self.data, end = ' ')
        if self.left:
            self.left.inorder_traversal()
        if self.right:
            self.right.inorder_traversal()
    
    def postorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        if self.right:
            self.right.inorder_traversal()
        print(self.data, end = ' ')

bst = BinarySearchTree(1)
bst.insert(2)
bst.insert(3)
bst.insert(4)
bst.inorder_traversal()
print()
bst.preorder_traversal()
print()
bst.postorder_traversal()