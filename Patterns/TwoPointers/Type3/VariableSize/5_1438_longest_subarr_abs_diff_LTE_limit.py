"""
LeetCode 1438: Longest Subarray with Absolute Diff Less Than or Equal to Limit
Question:
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of the subarray is less than or equal to limit.

Example:
Input: nums = [8,2,4,7], limit = 4
Output: 2

Explanation:
The subarray [2,4] has the maximum length since the absolute difference between any two elements is less than or equal to 4.

"""

from collections import deque

def longestSubarray(nums, limit):
    # init
    left = 0
    right = 0
    max_length = 0
    max_queue = deque()
    min_queue = deque()
    
    while right < len(nums):
        # expand the window
        while max_queue and nums[max_queue[-1]] < nums[right]:
            max_queue.pop()
        while min_queue and nums[min_queue[-1]] > nums[right]:
            min_queue.pop()
        max_queue.append(right)
        min_queue.append(right)
        right += 1
        
        # shrink the window
        while nums[max_queue[0]] - nums[min_queue[0]] > limit:
            if max_queue[0] == left:
                max_queue.popleft()
            if min_queue[0] == left:
                min_queue.popleft()
            left += 1
        
        # update the max length
        max_length = max(max_length, right - left + 1)
    
    return max_length

print(longestSubarray([8,2,4,7], 4))
print(longestSubarray([10,1,2,4,7], 5))