"""
Leetcode 344: Reverse String

Question:
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

def reverseString(s):
    """
    modify s in-place 
    """

    # init
    L = 0
    R = len(s) - 1

    while L < R:
        s[L], s[R] = s[R], s[L]
        L += 1
        R -= 1
    return s

print(reverseString(["h","e","l","l","o"]))
print(reverseString(["H","a","n","n","a","h"]))