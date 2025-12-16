"""
Leetcode 977: Squares of a Sorted Array

Question:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
"""


def sortedSquares(nums):

    # init
    L = 0
    R = len(nums) - 1
    pos = len(nums) - 1
    result = [0] * len(nums)

    while L <= R:
        # compare the abs values and then place the larger val
        if abs(nums[L]) > abs(nums[R]):
            result[pos] = (nums[L] * nums[L])
            L += 1
        else:
            result[pos] = (nums[R] * nums[R])
            R -= 1
        pos -= 1

    return result

print(sortedSquares([-4,-1,0,3,10]))
print(sortedSquares([-7,-3,2,3,11]))
