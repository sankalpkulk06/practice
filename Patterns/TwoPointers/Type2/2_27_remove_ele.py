"""
Leetcode 27: Remove Element

Question:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do this by modifying the input array in-place with O(1) extra memory.

example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

def removeElement(nums, val):
    # init
    L = 0
    R = 0

    while R < len(nums):
        # check if the current element (right pointer) is NOT equal to val
        if nums[R] != val:
            # swap the current element (left pointer) with the element (right pointer)
            # keep the valid ele on the left side of the array
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
        R += 1
    return L, nums

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))