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

"""
Tracing:

nums = [1,0,1,0,1], goal = 2

init:
prefix_sum = 0
ans = 0
count = {0: 1}

1. num = 1
prefix_sum = 1
count = {0: 1, 1: 1}
ans = 0

2. num = 0
prefix_sum = 1
count = {0: 1, 1: 2}
ans = 0

3. num = 1
prefix_sum = 2
since prefix_sum - goal = 0, ans += count[0] = 1
count = {0: 1, 1: 2, 2: 1}
ans = 0 + 1 = 1

4. num = 0
prefix_sum = 2
since prefix_sum - goal = 0, ans += count[0] = 1
count = {0: 1, 1: 2, 2: 2}
ans = 1 + 1 = 2

5. num = 1
prefix_sum = 3
since prefix_sum - goal = 1, ans += count[1] = 2
count = {0: 1, 1: 2, 2: 2, 3: 1}
ans = 2 + 2 = 4

"""