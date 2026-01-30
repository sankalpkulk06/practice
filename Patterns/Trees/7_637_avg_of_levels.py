"""
LC 637: Average of Levels in Binary Tree

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
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
    
    def averageOfLevels(self, root):
        """
        Approach:
        BFS with depth: [[3], [9,20], [15,7]]
        res = [3, 14.5, 11]

        Phase 1: BFS with depth
        Phase 2: take avgerage of the values in the nested lists
        """
        from collections import deque
        # base case
        if not root:
            return []
        
        # init
        q = deque([(root, 0)])
        bfs = []
        
        # Phase 1: BFS with depth
        while q:
            # pop left node and depth
            node, depth = q.popleft()

            # if depth is not in bfs, add it
            if len(bfs) == depth:
                bfs.append([])
            # append node to the depth
            bfs[depth].append(node.val)
            
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        
        # Phase 2: take avgerage of the values in the nested lists
        res = []
        for level in bfs:
            res.append(sum(level) / len(level))
        
        return res

    def optimal_averageOfLevels(self, root):
        """
        More Optimal:

        While doing BFS:
            - Level size = len(queue)
            - Pop exactly level size nodes
            - Accumulate level sum
            - Calc the average
            - Append average to result

        TC: O(n)
        SC: O(width of the tree)
        """
        from collections import deque
        # base case
        if not root:
            return []
        
        # init
        q = deque([root])
        res = []

        while q:
            # geet level size and init sum
            level_size = len(q)
            level_sum = 0

            # pop exactly level size nodes
            for _ in range(level_size):
                node = q.popleft()
                level_sum += node.val

                # add children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # calc the average
            res.append(level_sum / level_size)
        return res


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(root.averageOfLevels(root))
    print(root.optimal_averageOfLevels(root))
    root.printTree()