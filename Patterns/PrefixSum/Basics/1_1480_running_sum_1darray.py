"""
Leetcode 1480: Running Sum of 1D Array

Question:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

"""

def runningSum(nums):
    running_sum = []
    curr_sum = 0

    for num in nums:
        curr_sum += num
        running_sum.append(curr_sum)
    
    return running_sum

print(runningSum([1,2,3,4]))
print(runningSum([1,1,1,1,1]))
print(runningSum([3,1,2,10,1]))