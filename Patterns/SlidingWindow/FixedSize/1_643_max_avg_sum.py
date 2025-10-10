"""
Traced sliding window for LeetCode 643 (Maximum Average Subarray I)

Question:
Given an array nums and integer k, find the contiguous subarray of length k that has the maximum average value and return this value.

Example:
Input: nums = [1, 12, -5, -6, 50, 3], k = 4
Output: 12.75

"""

from typing import List

def findMaxAverage_traced(nums: List[int], k: int) -> float:
 
    # initial window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # slide the window
    for i in range(k, len(nums)):
        # print(nums[i]) # print the incoming element

        # slide the window
        # add next right and subtract the left most 
        window_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum/k

# --- Run the trace on the example ---
nums = [1, 12, -5, -6, 50, 3]
k = 4
avg = findMaxAverage_traced(nums, k)
print(avg)

# Try another quick case
nums2 = [5, 5, 5, 5, 5]
k2 = 3
avg2 = findMaxAverage_traced(nums2, k2)
print(avg2)

"""
Question:
1. Why cant we just use brute force here?
Answer:
    Brute force:
    - We can use a nested loop to check all possible subarrays of length k.
    - This will take O(n*k) time.
    - We can optimize this by using a sliding window.

2. What is the time complexity of the sliding window approach?
Answer:
    - The time complexity of the sliding window approach is O(n).

3. What happens if k = len(nums)?
Answer:
    - If k = len(nums), we will return the average of the entire array.

4. What happens if k = 1?
Answer:
    - If k = 1, we will return the maximum element in the array.

"""