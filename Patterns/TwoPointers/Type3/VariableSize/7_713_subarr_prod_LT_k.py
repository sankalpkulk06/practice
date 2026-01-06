"""
LeetCode 713: Subarray Product Less Than K
Question:
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

"""

def numSubarrayProductLessThanK(nums, k):
    # init
    L, R, ans = 0, 0, 0
    prod = 1

    if k <= 1:
        return 0

    # slide the window
    while R < len(nums):
        # expand the window
        prod *= nums[R]
        while prod >= k:
            prod /= nums[L]
            L += 1
        ans += R - L + 1
        R += 1
    return ans

print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(numSubarrayProductLessThanK([1, 2, 3], 0))
print(numSubarrayProductLessThanK([1, 1, 1], 2))