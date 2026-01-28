"""
- DFS from a Given Source of Undirected Tree
- Uses a Recursive approach for the recursive implementation
- Uses a Stack for iterative implementation
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def recursive_dfs(self, root):
        if root is None:
            return
        # Pre-order DFS: root -> left -> right
        print(root.val, end=" ")
        self.recursive_dfs(root.left)
        self.recursive_dfs(root.right)

    def iterative_dfs(self, root):
        if root is None:
            return
        # Pre-order DFS using a stack (push right first, so left is processed first)
        stack = [root]
        while stack:
            node = stack.pop()
            print(node.val, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("Recursive DFS:")
    root.recursive_dfs(root)
    print("\nIterative DFS:")
    root.iterative_dfs(root)