"""
94. Binary Tree Inorder Traversal
"""

def inorderTrav(root):
    res = []

    def inorder(root):
        if root is None:
            return

        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res

print(inorderTrav([1,None,2,3]))