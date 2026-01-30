"""
LC 199: Right Side View of a Binary Tree

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
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

    def rightSideView(self, root):
        """
        After creating a BFS res which is org with depth,
        result will be -1 index of all the nested lists (depth)
        So we can traverse through the res and get -1 index of each list and append it to the result
        return the result

        BFS: [[1], [2,3], [5,4]]
        res: [1,3,4]

        BFS: [[1], [2,3], [4], [5]]
        res: [1,3,4,5]
        """
        from collections import deque
        # base case
        if not root:
            return []
        
        # init
        q = deque([(root, 0)])
        bfs = []

        # Phase 1: BFS
        while q:
            # pop left node and depth
            node, depth = q.popleft()

            # if depth is not in bfs, add it
            if len(bfs) == depth:
                bfs.append([])
            # append node to the depth
            bfs[depth].append(node.val)

            # add children
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        
        # Phase 2: to get all the right side view nodes, get -1th index of each nested list in bfs
        res = []
        for level in bfs:
            res.append(level[-1])
        
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    print(root.rightSideView(root))