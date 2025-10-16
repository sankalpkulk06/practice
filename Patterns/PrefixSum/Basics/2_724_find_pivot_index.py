"""
Leetcode 724: Find Pivot Index

Question:
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

"""


def findPivotIndex(nums):

    total_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        # because total sum = left sum + nums[i] + right sum 
        right_sum = total_sum - left_sum - nums[i]

        if left_sum == right_sum:   # pivot index found
            return i

        left_sum += nums[i]
    
    return -1

print(findPivotIndex([1,7,3,6,5,6]))
print(findPivotIndex([1,2,3]))
print(findPivotIndex([2,1,-1]))
