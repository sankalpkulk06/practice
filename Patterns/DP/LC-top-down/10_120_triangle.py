"""
Leetcode 120. Triangle

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
    [2]
    [3,4]
    [6,5,7]
    [4,1,8,3]
    The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.
"""

class Solution:
    def minimumTotal(self, triangle):
        """
        Memoization approach:
        - init memo
        - store (r,c) in memo

        Base case:
        - if row == len(triangle) - 1, return the num

        Recurring Logic:
        - number + min( (index i of next row), (index i+1 of next row) )
        """

        # init memo
        memo = {}

        # helper function
        def soln(r,c):
            # base case
            if r == len(triangle) - 1:
                return triangle[r][c]
            
            # memo base case
            if (r,c) in memo:
                return memo[(r,c)]

            # recurring logic
            memo[(r,c)] = triangle[r][c] + min(soln(r+1, c), soln(r+1, c+1))    
            return memo[(r,c)]

        return soln(0,0)
        

if __name__ == "__main__":
    print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(Solution().minimumTotal([[-10]]))
