"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example:
Input: p = [1,2,3], q = [1,2,3]
Output: true
"""

def isSameTree(p,q):
    res1 = []
    res2 = []
    def inorder(root, res):
        if root is None:
            return

        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(p, res1)
    inorder(q, res2)
    return res1 == res2

print(isSameTree([1,2,3], [1,2,3]))
print(isSameTree([1,3,4], [1,2,3]))