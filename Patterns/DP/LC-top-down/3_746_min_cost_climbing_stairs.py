"""
Leetcode 746. Min Cost Climbing Stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: You will start from index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: You will start from index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb two steps to reach index 8.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Example 3:
Input: cost = [0, 0, 0, 0]
Output: 0
Explanation: You will start from index 0.
- Pay 0 and climb one step to reach the top.
The total cost is 0.
"""

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        Memoization approach:
        - use a dictionary to store the results of the min cost climbing stairs
        - if the result is already in the memo, return it
        - otherwise, calculate the result and store it in the memo and then return it
        """
        # memoization
        memo = {}
        # helper function
        def solution(idx):
            if idx in memo:
                return memo[idx]

            if idx >= len(cost):
                return 0

            memo[idx] = min(solution(idx + 1), solution(idx + 2)) + cost[idx]
            return memo[idx]

        # return min(solution(0), solution(1))
        return min(solution(0), memo[1])

if __name__ == "__main__":
    print(Solution().minCostClimbingStairs([10, 15, 20])) # 15
    print(Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])) # 6
    print(Solution().minCostClimbingStairs([0, 0, 0, 0])) # 0
    print(Solution().minCostClimbingStairs([0, 1, 0, 1])) # 0