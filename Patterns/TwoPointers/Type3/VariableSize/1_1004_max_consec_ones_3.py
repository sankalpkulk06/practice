"""
LeetCode 1004: Max Consecutive Ones III

Question:
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6

"""

def maxConsecutiveOnes(nums, k):
    
    # init pointers
    left = 0
    zeros = 0
    best = 0

    # slide the window
    for right in range(len(nums)):
        # if the current element is a 0, increment the zeros count
        # expand the window
        if nums[right] == 0:
            zeros += 1

        # if the zeros count is greater than k, increment the left pointer
        # shrink the window (INVALID)
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1

        # update the best
        best = max(best, right - left + 1)

    return best


nums = [1,1,1,0,0,0,1,1,1,1,0]
res = maxConsecutiveOnes(nums, 2)
print(res)

nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
res2 = maxConsecutiveOnes(nums2, 3)
print(res2)

nums3 = [0,0,1,0,0,1]
res3 = maxConsecutiveOnes(nums3, 2)
print(res3)

nums4 = [1,1,1,1,1]
res4 = maxConsecutiveOnes(nums4, 0)
print(res4)

nums5 = [0,0,0,0,0]
res5 = maxConsecutiveOnes(nums5, 3)
print(res5)

"""
Pattern: variable sliding window

eg. nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
can flip only 2 zeros

[1,1,1], zeros = 0, len = 3
[1,1,1,0], zeros = 1, len = 4
[1,1,1,0,0], zeros = 2, len = 5
[1,1,1,0,0,0], zeros = 3, len = 6 (INVALID)
shift L till zeros is less than k
[1,1,0,0,0] (INVALID)
[1,0,0,0] (INVALID)
...
[0,0], zeros = 2, len = 2
[0,0,1], zeros = 2, len = 3
...
[0,0,1,1,1,1], zeros = 2, len = 6
[0,0,1,1,1,1,0], zeros = 3, len = 7 (INVALID)
shift L till zeros is less than k
[0,1,1,1,1,0], zeros = 2, len = 6

ANS = 6

Thought process:
- init zeros (which stores the num of zeros in window), and max_len (stores the max length of window)
- init L, R = 0, 0
- while R < len(nums):
    - if the incoming num (R) is 0: then zeros += 1
    - if the number of zeros is GT k, we need to move L pointer till zeros is LTE k. so, while zeros > k:
        - if left (exiting) num is 0: then decrement zeros
        - increment L pointer

    - max_len = max(max_len, R - L + 1)
    - R += 1

- return max_len
"""