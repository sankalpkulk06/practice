"""
LC 104: Max Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        
        maxDepthLeft = self.maxDepth(root.left)
        maxDepthRight = self.maxDepth(root.right)

        return 1 + max(maxDepthLeft, maxDepthRight)

# Test cases
if __name__ == "__main__":
    # Test case 1
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().maxDepth(root))  # Output: 3