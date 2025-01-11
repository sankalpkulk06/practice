"""
111. Minimu Depth
"""

def minDepth(self, root) -> int:
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1

    if root.left:
        leftdepth = self.minDepth(root.left)
    else:
        leftdepth = float('inf')
    
    if root.right:
        rightdepth = self.minDepth(root.right)
    else:
        rightdepth = float('inf')

    return min(leftdepth, rightdepth) + 1