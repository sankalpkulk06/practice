"""
Leetcode 26: Remove Duplicates from Sorted Array

Question:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

def removeDuplicates(nums):
    # init
    L = 0
    R = 1

    while R < len(nums):
        # since nums is sorted
        # just check if the current element (right pointer) is NOT equal to the previous element (left pointer)
        if nums[R] != nums[L]:
            L += 1
            nums[L] = nums[R]
        R += 1
    return L + 1, nums

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))