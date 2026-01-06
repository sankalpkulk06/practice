"""
LeetCode 209: Minimum Size Subarray Sum

Question:
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [nums[l], nums[l+1], ..., nums[r-1], nums[r]] of which the sum is greater than or equal to target. If there isn't one, return 0 instead.

Example:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

"""

"""
Pattern: Variable Sliding Window

eg.
target = 7, nums = [2,3,1,2,4,3]

[2], sum = 2, len = 1
[2,3], sum = 5, len = 2
[2,3,1], sum = 6, len = 3
[2,3,1,2], sum = 8, len = 4 (VALID - not best)
move left to find the smallest len
[3,1,2], sum = 6, len = 3
move right again
[3,1,2,4], sum = 10, len = 4 
move left to find smallest len
[1,2,4], sum = 7, len = 3
[2,4], sum = 6, len = 2
move right
[2,4,3], sum = 9, len = 3
move left to find smallest len
[4,3], sum = 7, len = 2

Thought process:
- init L, R = 0, 0
- init best_len, window_sum = len(nums) + 1, 0
- while R < len(nums):
    - add incoming num to window_sum
    - if the window_sum is GT target then we will shrink the window to find the smallest len which meets condition
        while window_sum > target:
            - best_len = min(best_len, R - L + 1)
            -  subtract the exiting num from window_sum
            - inc L += 1
    - R += 1
- if solution was never reached i.e the best_len is still len(nums) + 1
- return best_len
"""

def minSubArrayLen(target, nums):
    # init
        L, R, best_len, window_sum = 0, 0, len(nums) + 1, 0

        while R < len(nums):
            # add incoming num to window_sum
            window_sum += nums[R]

            # shrink window to find opt soln
            while window_sum >= target:
                # get best soln
                best_len = min(best_len, R - L + 1)
                # subtract the exiting num
                window_sum -= nums[L]
                L += 1
            R += 1
        
        # if the solution wasnt reached
        if best_len == len(nums) + 1:
            return 0
        return best_len

print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(4, [1,4,4]))
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))