"""
Leetcode 283: Move Zeroes

Question:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

def moveZeroes(nums):

    # init
    L = 0
    R = 0

    while R < len(nums):
        # if non-zero, swap with the left pointer
        # print(f"{L}: {nums[L]}, {R}: {nums[R]}, {nums}")
        if nums[R] != 0:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1 # move left pointer to next non-zero element
        R += 1 # move right pointer to next element
    return nums

print(moveZeroes([0,1,0,3,12]))
print(moveZeroes([0]))
print(moveZeroes([0,0,1]))
print(moveZeroes([0,0,0,0,12]))