"""
Preorder traversal visits the node in the order: Root -> Left -> Right
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preorder(root):
    
    # if the tree is null (empty)
    if root is None:
        return



    # Recursive call on right subtree
    preorder(root.right)

    # visit current node
    print(root.data, end=" ")

    # Recursive call on left subtree
    preorder(root.left)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
preorder(root)