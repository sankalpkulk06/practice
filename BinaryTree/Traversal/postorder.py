"""
Post traversal visits the node in the order:  Left -> Right -> Root
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):
    
    # if the tree is null (empty)
    if root is None:
        return

    # Recursive call on left subtree
    postorder(root.left)

    # Recursive call on right subtree
    postorder(root.right)

    # visit current node
    print(root.data, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
postorder(root)