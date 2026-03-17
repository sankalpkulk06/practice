"""
Leetcode 62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

class Solution:
    def uniquePaths(self, m, n):
        """

        Memoization approach:
        - init memo

        base cases:
        - if m == 0 or n == 0, return 0
        - if m == 1 and n == 1, return 1

        recursive sub problems:
        - sum soln(m-1, n) and soln(m, n-1)

        before returning, store the result in memo[m][n]
        """

        # init memo
        memo = {}

        # helper function
        def soln(m, n):
            if (m, n) in memo:
                return memo[(m, n)]

            if m == 0 or n == 0:
                return 0

            if m == 1 and n == 1:
                return 1

            memo[(m,n)] = soln(m-1, n) + soln(m, n-1)
            return memo[(m,n)]

        return soln(m, n)

if __name__ == "__main__":
    print(Solution().uniquePaths(3, 7)) # 28
    print(Solution().uniquePaths(3, 2)) # 3
    print(Solution().uniquePaths(7, 3)) # 28
    print(Solution().uniquePaths(3, 3)) # 6
    print(Solution().uniquePaths(1, 1)) # 1
    print(Solution().uniquePaths(1, 2)) # 1
    print(Solution().uniquePaths(2, 1)) # 1
    print(Solution().uniquePaths(2, 2)) # 2
    print(Solution().uniquePaths(2, 3)) # 3
    print(Solution().uniquePaths(3, 2)) # 3