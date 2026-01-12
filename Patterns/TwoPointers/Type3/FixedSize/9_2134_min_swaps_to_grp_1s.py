"""
LC 2134: Minimum Swaps to Group All 1's Together

Question:
You are given a binary array nums.
You are allowed to perform two types of operations on the array:
1. Swap any two adjacent elements.
2. Flip any element.

Return the minimum number of operations needed to group all 1's together in the array.

Example 1:
Input: nums = [1,0,1,0,1]
Output: 1

"""

def minSwaps(nums):
    # init
    total_ones = sum(nums)
    window_size = total_ones
    ones_in_window = sum(nums[:window_size])
    max_ones = ones_in_window

    # slide window
    for i in range(window_size, len(nums)):
        L = i - window_size
        R = i
        ones_in_window -= nums[L % len(nums)]
        ones_in_window += nums[R % len(nums)]
        max_ones = max(max_ones, ones_in_window)
    
    return total_ones - max_ones


print(minSwaps([1,0,1,0,1]))
print(minSwaps([1,0,1,0,1,0,0,1,1,0,1]))
print(minSwaps([0,1,1,1,0,0,1,1,0]))
print(minSwaps([1,1,0,0,1]))
print(minSwaps([1,1,1,1,0]))
print(minSwaps([0,1,0,1,1,0,0,1,1,0,1]))
print(minSwaps([1,0,1,0,1,0,0,1,1,0,1]))
print(minSwaps([0,1,1,1,0,0,1,1,0]))
print(minSwaps([1,1,0,0,1]))
print(minSwaps([1,1,1,1,0]))

"""
Goal:
num of swaps = num of 0's in the window (minimum number of 0's in the window)

Thought Process:
	○ Lets start by counting the number of 1 in the list and store it as "total_ones" this can be found easily by summing the list
	○ So now the window size if "total_ones"
	○ Init window
	○ Ones_in_window = sum[0:total_ones]
	For start from 0 to n - 2:
		•	leaving = start
		•	entering = start + k
		•	Update using circular indexing:
		•	ones_in_window -= nums[leaving % n]
		•	ones_in_window += nums[entering % n]
		•	max_ones = max(max_ones, ones_in_window)
	○ The best window has max_ones ones, so it has k - max_ones zeros
	○ Each zero inside the chosen window needs one swap with a one outside
    Answer = k - max_ones

"""