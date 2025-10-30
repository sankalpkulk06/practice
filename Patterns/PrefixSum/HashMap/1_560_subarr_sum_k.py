"""
Leetcode 560: Subarray Sum Equals K

Question:
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2

"""
from collections import defaultdict

def subarraySum(nums, k):
    prefix_sum = 0
    result = 0
    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1

    for num in nums:
        # calculate prefix sum
        prefix_sum += num

        # check if the prefix sum - k exists in the prefix sum count
        # if it does, it means there is a subarray that sums to k
        if prefix_sum - k in prefix_sum_count:
            result += prefix_sum_count[prefix_sum - k]
        # add the prefix sum to the prefix sum count
        prefix_sum_count[prefix_sum] += 1

    return result

print(subarraySum([1,1,1], 2))