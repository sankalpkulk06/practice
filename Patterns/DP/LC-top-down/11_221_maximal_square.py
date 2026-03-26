"""
Leetcode 221. Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1
"""

class Solution:
    def maximalSquare(self, matrix):
        """ 
        Memoization:
        - store r,c in memo and 
        
        Base case:
        - if out of bounds, return 0

        Recursive subproblem:
        - if (r,c) is 1:
            - 1 + min ( down, right, diagonal )

        """

        # memo
        memo = {}

        # init
        rows = len(matrix)
        cols = len(matrix[0])

        # helper
        def soln(r, c):
            # if out of bounds
            if r >= rows or c >= cols:
                return 0
            
            # if subprob not in memo
            if (r,c) not in memo:
                # next pos
                right = soln(r+1, c)
                down = soln(r, c+1)
                diagonal = soln(r+1, c+1)

                memo[(r,c)] = 0
                if matrix[r][c] == "1":
                    memo[(r,c)] = 1 + min(right, down, diagonal)
            
            return memo[(r,c)]
        
        soln(0,0)
        return max(memo.values()) ** 2

if __name__ == "__main__":
    print(Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(Solution().maximalSquare([["0","1"],["1","0"]]))