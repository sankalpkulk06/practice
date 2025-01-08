"""
101. Symmetric Tree


"""

class Solution:
    def isSymmetric(self, root) -> bool:
        
        def isMirror(n1, n2):   # n1- left, n2- right
            if not n1 and not n2:
                return True
            
            if not n1 or not n2:
                return False

            return n1.val == n2.val and isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)
        
        return isMirror(root.left, root.right)