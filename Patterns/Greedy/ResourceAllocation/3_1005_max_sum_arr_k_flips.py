"""
leetcode 1005: Maximize Sum Of Array After K Negations

Question:
Given an integer array nums and an integer k, modify the array in the following way:
select an index i and replace nums[i] with -nums[i].

Return the maximum possible sum of the array after modifying it in this way.

Example 1:
Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 1 and nums becomes [4,-2,3].
"""

def maxSumAfterKNegations(nums, k):
    # sort the array
    nums.sort()
    # print(nums)

    # flip negatives while possible
    for i in range(len(nums)):
        if nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
        else:
            break
    
    total = sum(nums)
    # remaining flips
    if k > 0:
        # if k is odd, flip the smallest element (min abs value)
        if k % 2 == 1:
            smallest = min(nums, key=abs)
            total -= 2 * abs(smallest)

    return total

print(maxSumAfterKNegations([4,2,3], 1))
print(maxSumAfterKNegations([4,2,3], 2))
print(maxSumAfterKNegations([4,2,3], 3))
print(maxSumAfterKNegations([4,2,3], 4))
print(maxSumAfterKNegations([4,2,3], 5))
print(maxSumAfterKNegations([4,2,3], 6))
print(maxSumAfterKNegations([4,2,3], 7))
print(maxSumAfterKNegations([4,2,3], 8))
print(maxSumAfterKNegations([4,2,3], 9))
print(maxSumAfterKNegations([4,2,3], 10))