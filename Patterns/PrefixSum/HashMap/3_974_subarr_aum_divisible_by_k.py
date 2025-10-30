"""
Leetcode 974: Subarray Sums Divisible by K

Question:
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
"""

from collections import defaultdict

def subarraysDivByK(nums, k):
    # init
    prefix_sum = 0 # prefix sum
    ans = 0
    count = defaultdict(int) # count of prefix sums modulo k
    count[0] = 1 # because 0 is divisible by k

    for num in nums:
        # calculate prefix sum
        prefix_sum += num

        # check if the prefix sum modulo k exists in the count
        # if it does, it means there is a subarray that sums to a multiple of k
        if prefix_sum % k in count:
            ans += count[prefix_sum % k]

        # add the prefix sum modulo k to the count
        count[prefix_sum % k] += 1
        
    return ans


print(subarraysDivByK([4,5,0,-2,-3,1], 5))