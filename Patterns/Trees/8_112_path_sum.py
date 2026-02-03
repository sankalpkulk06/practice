"""
LC 112: Path Sum

Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def hasPathSum(self, root, targetSum):
        """
        Helper function needed because we need to also pass current sum to the recursive function

        base case:
        - if the node is None, return False

        logic:
        - add the node's value to the current sum
        - if the node is a leaf and the current sum equals the target sum, return True
        - otherwise, return the result of the left and right subtrees

        wrap all this in a helper function and return the result of the helper function
        """

        def dfs(node, currSum):
            # base case
            if not node: 
                return False
            
            # add node val to current sum
            currSum += node.val

            # if node is leaf and currSum equals targetSum, return True
            if not node.left and not node.right and currSum == targetSum:
                return True
            
            # traverse left and right subtrees
            L = dfs(node.left, currSum)
            R = dfs(node.right, currSum)

            # return True if either left or right subtree has a path sum equal to targetSum
            return L or R
        
        return dfs(root, 0)


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(root.hasPathSum(root, 22))
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(3)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    print(root.hasPathSum(root, 22))