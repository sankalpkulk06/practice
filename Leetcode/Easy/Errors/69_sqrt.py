"""
69. Sqrt(x) (TIME EXCEEDED)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
"""

"""
Logic:
- Use binary search: O(logn)

x = 7

0....7

mid^2 > X? Lesser

0...Mid-1

mid^2 < X - search right side

mid^2 == X, return mid

"""

def mySqrt(x):

    l, r = 0, x
    res = 0

    while l <= r:
        mid = l + ((r-1) // 2)  # will never overflow

        if mid**2 > x:
            r = mid - 1
        elif mid**2 < x:
            l = mid + 1
            res = mid
        else:
            return mid
    return res


print(mySqrt(8))
