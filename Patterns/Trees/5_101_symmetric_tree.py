"""
LC 101. Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def isSymmetric(self, root):
        """
        Base cases:
        - if both nodes are None, return true
        - if only one of the nodes is None, return false

        Logic:
        return True if:
            - both node1 and node 2 are equal
            - mirror(node1.left, node2.right) 
            - and mirror(node1.right, node2.left)
        return False otherwise

        wrap all this in a helper function and return the result of the helper function
        """
        
        def isMirror(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
        
        return isMirror(root.left, root.right)

if __name__ == "__main__":
    # Test case 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(root.isSymmetric(root))
    # Test case 2
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    print(root.isSymmetric(root))