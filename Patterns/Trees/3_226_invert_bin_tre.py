"""
LC 226: Invert Binary Tree

Given the root of a binary tree, invert the tree, and return its root.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def printTree(self):
        print(self.val, end=" ")
        if self.left:
            self.left.printTree()
        if self.right:
            self.right.printTree()

class Solution:
    def invertTree(self, root):
        """
        Base case:
        - If the node is None, return None

        - traverse the left and right subtrees
        - swap the left and right subtrees
        - return the root
        """
        
        # Base case: if the node is None, return None
        if not root: 
            return None
        
        # traverse the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # swap the left and right subtrees
        root.left, root.right = root.right, root.left
        
        # return the root
        return root

# Test cases
if __name__ == "__main__":
    # Test case 1
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    print("Original tree: ", end="")
    root.printTree()  # Output: [4,2,7,1,3,6,9]
    Solution().invertTree(root)
    print("\nInverted tree: ", end="")
    root.printTree()  # Output: [4,7,2,9,6,3,1]