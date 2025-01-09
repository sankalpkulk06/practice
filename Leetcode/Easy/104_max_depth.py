"""
104. Max Depth of a Tree
"""
class Solution:
    def maxDepth(self, root):
        
        if not root:
            return 0

        maxDepthLeft = self.maxDepth(root.left)
        maxDepthRight = self.maxDepth(root.right)

        return max(maxDepthLeft, maxDepthRight) + 1