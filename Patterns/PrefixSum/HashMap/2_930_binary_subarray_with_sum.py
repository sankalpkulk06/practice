"""

Leetcode 930: Binary Subarrays With Sum

Question:
Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

A subarray is a contiguous part of an array.

 
Example 1:

Input: nums = [1,0,1,0,1], goal = 2
Output: 4

"""
from collections import defaultdict

def numSubarraysWithSum(nums, goal):
    prefix_sum = 0
    ans = 0
    count = defaultdict(int)
    count[0] = 1
    for num in nums:
        # calculate prefix sum
        prefix_sum += num

        # check if the prefix sum - goal exists in the count
        # if it does, it means there is a subarray that sums to goal
        if prefix_sum - goal in count:
            ans += count[prefix_sum - goal]
            
        # add the prefix sum to the count
        count[prefix_sum] += 1
    return ans

print(numSubarraysWithSum([1,0,1,0,1], 2))