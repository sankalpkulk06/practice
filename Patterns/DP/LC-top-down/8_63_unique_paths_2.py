"""
Leetcode 63. Unique Paths II

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        Memoization approach:
        - init memo

        base cases:
        - if the current cell is an obstacle, return 0
        - if the current cell is out of bounds, return 0
        - if the current cell is the bottom-right corner, return 1

        recursive sub problems:
        - sum soln(m-1, n) and soln(m, n-1)
        """
        # init memo
        memo = {}
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # base case
        if obstacleGrid[0][0] == 1:
            return 0

        # helper function
        def soln(m, n):
            if (m, n) in memo:
                return memo[(m, n)]
            if m < 0 or n < 0 or obstacleGrid[m][n] == 1:
                return 0
            if m == 0 and n == 0:
                return 1
            memo[(m, n)] = soln(m-1, n) + soln(m, n-1)
            return memo[(m, n)]

        return soln(m-1, n-1)
if __name__ == "__main__":
    print(Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])) # 2
    print(Solution().uniquePathsWithObstacles([[0,1],[0,0]])) # 1
    print(Solution().uniquePathsWithObstacles([[0,0],[0,1]])) # 0
    print(Solution().uniquePathsWithObstacles([[0,0],[0,0]])) # 2
    print(Solution().uniquePathsWithObstacles([[0,0],[0,0]])) # 2
    print(Solution().uniquePathsWithObstacles([[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]])) # 0
