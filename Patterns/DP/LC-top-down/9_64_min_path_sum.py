"""
Leetcode 64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""

class Solution:
    def minPathSum(self, grid):
        """
        Memoization approach:

        Base case:
        - if out of bounds return "+ infinity"

        core logic:
        - cost + min(down, left)

        memoize it:
        - store (m,n) in memo
        - before resturning, store it
        """

        # init memo
        memo = {}

        # helper function
        def soln(m, n):
            # check if in memo
            if (m, n) in memo:
                return memo[(m, n)]

            # base cases
            # if out of bounds return "+ infinity"
            if m >= len(grid) or n >= len(grid[0]): # out of bounds 
                return float('inf')

            # if at the bottom-right corner, return the cost at that cell
            if m == len(grid) - 1 and n == len(grid[0]) - 1:
                return grid[m][n]
            
            # store in memo
            memo[(m, n)] = grid[m][n] + min(soln(m+1, n), soln(m, n+1))
            return memo[(m, n)]
        
        return soln(0,0) # start at the top-left corner
    
if __name__ == "__main__":
    print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
    print(Solution().minPathSum([[1,2,3],[4,5,6]]))