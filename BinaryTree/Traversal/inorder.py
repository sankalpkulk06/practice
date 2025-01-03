"""
- Inorder traversal visits the node in the order: Left -> Root -> Right

Pseudo code (Algorithm):
- Traverse the left subtree, i.e., call Inorder(left->subtree) 
- Visit the root. 
- Traverse the right subtree, i.e., call Inorder(right->subtree) 

Uses of Inorder Traversal:
- In the case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order.
- To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal is reversed can be used.
- Inorder traversal can be used to evaluate arithmetic expressions stored in expression trees.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    
    # if the tree is null (empty)
    if root is None:
        return

    # Recursive call on left subtree
    inorder(root.left)

    # visit current node
    print(root.data, end=" ")

    # Recursive call on right subtree
    inorder(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inorder(root)