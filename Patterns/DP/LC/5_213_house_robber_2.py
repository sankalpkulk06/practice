"""
Leetcode 213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""

class Solution:
    def rob(self, nums):
        """
        Memoization approach:

        Base cases:
        - if index is >= len(nums), return 0

        Recursive sub problems:
        - what if we rob the current house?: nums[index] + solution(index + 2)
        - what if we don't rob the current house?: solution(index + 1)
        - return the max of the two

        Before returning, store the result in memo[idx]

        Consider two cases:
        - case 1: rob the first house and not the last house
        - case 2: don't rob the first house and rob the last house
        - return the max of the two
        """
        
        # init
        n = len(nums)

        # base case
        if n == 1:
            return nums[0]

        # helper function
        def robRange(start, end):
            # memoization
            memo = {}

            # helper function
            def soln(idx):
                if idx in memo:
                    return memo[idx]

                if idx >= end:
                    return 0
                
                robHouse = nums[idx] + soln(idx + 2)
                skipHouse = soln(idx + 1)

                memo[idx] = max(robHouse, skipHouse)
                return memo[idx]

            return soln(start)

        return max(robRange(0, n-1), robRange(1, n))

if __name__ == "__main__":
    print(Solution().rob([2,3,2])) # 3
    print(Solution().rob([1,2,3,1])) # 4    
    print(Solution().rob([1,2,3,4,5,1,2,3,4,5])) # 16
    print(Solution().rob([1,2,3,4,5,1,2,3,4,5,1,2,3,4,5])) # 24