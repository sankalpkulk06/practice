"""
Leetcode 11: Container With Most Water

Question:
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
"""

def maxArea(height):
    # init
    L = 0
    R = len(height) - 1
    max_water = 0

    while L < R:
        h = R - L
        w = min(height[L], height[R])

        max_water = max(max_water, h * w)
        # move the pointer that has the smaller height
        if height[L] < height[R]:
            L += 1
        else:
            R -= 1
    return max_water

    
    
print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))
print(maxArea([4,3,2,1,4]))
print(maxArea([1,2,1]))