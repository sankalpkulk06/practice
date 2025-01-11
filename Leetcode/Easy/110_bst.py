"""
Given a binary tree, determine if it is 
height-balanced
"""
def isBalanced(self, root) -> bool:
    
    def helper(root):
        if root is None:
            return 0

        left_height = helper(root.left)
        right_height = helper(root.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        
        return (max(left_height, right_height) + 1)
    
    return helper(root) != -1