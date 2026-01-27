"""
LC 100: Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
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
    def isSameTree(self, p, q):
        """
        Base case:
        - if both nodes are None, they are the same so return True
    
        - if only one of the nodes is None, they are not the same so return False

        - both nodes have the same value, so check the left and right subtrees
        - return the result of the left and right subtrees

        - if the values are not the same, return False
        """

        # Base case: if both nodes are None, they are the same
        #  so return True
        if not p and not q:
            return True
        
        # Base case: if only one of the nodes is None, they are not the same so return False
        if not p or not q:
            return False
        
        # both nodes have the same value, so check the left and right subtrees
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        # the values are not the same, they are not the same tree
        return False

# Test cases
if __name__ == "__main__":
    # Test case 1
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    print(Solution().isSameTree(p, q))  # Output: True