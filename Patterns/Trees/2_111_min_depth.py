"""
LC 111: Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root):
        """
        Base case:
        - If there is no toor, return 0
        
        # Case 1: if the node does not have any children, return 1
        # Case 2: if the node has only one child
            - if has only left child, return the min depth of the left child and set the right child to inf
            - if has only right child, return the min depth of the right child and set the left child to inf
        # Case 3: if the node has two children
            - return the min depth of the two children + 1
        """

        # Base case: if the node does not have any children, return 0
        if not root:
            return 0
        
        # Case 1: if the node has no children, return 1
        if not root.left and not root.right:
            return 1
        
        # Case 2: if the node has only one child
        if not root.left:   # has only right child
            return self.minDepth(root.right) + 1
        if not root.right:   # has only left child
            return self.minDepth(root.left) + 1
        
        # Case 3: if the node has two children
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# Test cases
if __name__ == "__main__":
    # Test case 1
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().minDepth(root))  # Output: 2
    # Test case 2
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    root.right.right.right.right = TreeNode(6)
    print(Solution().minDepth(root))  # Output: 5
