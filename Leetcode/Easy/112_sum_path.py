"""
112. Path Sum

Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""

def hasPathSum(root, targetSum):
    if root is None:
        return False

    targetSum -= root.val

    if not root.left and not root.right:
        return targetSum == 0
    
    return (hasPathSum(root.left, targetSum) or hasPathSum(root.right, targetSum))