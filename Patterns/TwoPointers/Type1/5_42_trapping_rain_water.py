"""
Leetcode 42: Trapping Rain Water

Question:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
"""

def trap(height):
    # init
    L = 0
    R = len(height) - 1
    left_max = height[L]
    right_max = height[R]
    water = 0

    while L < R:
        
        if left_max <= right_max: # move the left pointer, left wall is limiting the water
            L += 1
            left_max = max(left_max, height[L])
            # if next bar is taller than left wall, add the difference to the water (collected water)
            if left_max > height[L]:
                water += left_max - height[L]
        else:
            R -= 1
            right_max = max(right_max, height[R])
            # if next bar is taller than right wall, add the difference to the water (collected water)
            if right_max > height[R]:
                water += right_max - height[R]
    return water

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))