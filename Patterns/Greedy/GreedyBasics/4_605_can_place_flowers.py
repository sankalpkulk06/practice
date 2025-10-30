"""
Leetcode 605: Can Place Flowers 

Question:
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Explanation: There is only one space that can be used to plant a flower. Since there is only one space that can be used, we cannot plant 2 flowers.
"""
def canPlaceFlowers(flowerbed, n):
    if n == 0:
        return True
    m = len(flowerbed)
    for i in range(m):
        if flowerbed[i] == 0:
            left_empty  = (i == 0) or (flowerbed[i - 1] == 0)
            right_empty = (i == m - 1) or (flowerbed[i + 1] == 0)
            if left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1
                if n == 0:          
                    return True
    return n == 0

print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1], 2))
print(canPlaceFlowers([1,0,0,0,1], 3))
print(canPlaceFlowers([1,0,0,0,1], 4))
print(canPlaceFlowers([1,0,0,0,1], 5))
print(canPlaceFlowers([1,0,0,0,1], 6))
print(canPlaceFlowers([1,0,0,0,1], 7))
print(canPlaceFlowers([1,0,0,0,1], 8))
print(canPlaceFlowers([1,0,0,0,1], 9))
print(canPlaceFlowers([1,0,0,0,1], 10))
print(canPlaceFlowers([1,0,0,0,1], 11))
print(canPlaceFlowers([1,0,0,0,1], 12))

"""
Logic:
- if n is 0, return True
- traverse the flowerbed
- if the current plot is empty and the left and right plots are also empty, plant a flower and decrement n
- if n is 0, return True
- return False if n is not 0
"""