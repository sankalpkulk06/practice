"""

Leetcode 409: Longest Palindrome

Question:
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.


Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
from collections import Counter
def longestPalindrome(s):
    # init counter
    counter = Counter(s)
    # init length
    length = 0
    # traverse counter
    for count in counter.values():
        length += count // 2 * 2
        if length % 2 == 0 and count % 2 == 1:
            length += 1
    return length

print(longestPalindrome("abccccdd"))
print(longestPalindrome("a"))
print(longestPalindrome("aa"))
print(longestPalindrome("abccccdd"))
print(longestPalindrome("abccccdd"))