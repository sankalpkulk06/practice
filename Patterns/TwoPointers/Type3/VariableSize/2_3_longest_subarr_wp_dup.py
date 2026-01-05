"""
LeetCode 3: Longest Substring Without Repeating Characters

Question:
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3

"""

def longestSubstring(s: str) -> int:
    # init 
    last_occ = {}
    left = 0
    best = 0

    # bacab
    for right in range(len(s)):
        ch = s[right]
        if ch in last_occ and last_occ[ch] > left:
            # move left to last occurance of s[right] + 1
            left = last_occ[ch]
        last_occ[ch] = right + 1
        best = max(best, right - left + 1)
    return best

s = "bacab"
res = longestSubstring(s)
print(res)

s = "abcabcbb"
res2 = longestSubstring(s)
print(res2)
