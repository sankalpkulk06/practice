"""
Leetcode 125: Valid Palindrome

Question:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

def isPalindrome(s):
    # filter out non-alphanumeric characters
    filtered_str = [char.lower() for char in s if char.isalnum()]

    # if empty
    if not filtered_str:
        return True

    # init left and right pointers
    L = 0
    R = len(filtered_str) - 1

    while L < R:
        if filtered_str[L] == filtered_str[R]:
            L += 1
            R -= 1
        else:
            return False
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))