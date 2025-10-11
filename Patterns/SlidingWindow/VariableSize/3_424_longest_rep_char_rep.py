"""
LeetCode 424: Longest Repeating Character Replacement
Question:
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example:
Input: s = "AABABBA", k = 1
Output: 4

"""
from collections import defaultdict

def longestRepCharRep(s: str, k: int) -> int:

    # init pointers
    count = defaultdict(int)    # countof all the char in the current window
    left = 0
    best = 0
    max_count = 0               # max count of any char in the current window
    
    # slide the window
    for right in range(len(s)):
        # expand the window
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])

        # shrink the window (INVALID)
        if right - left + 1 - max_count > k:
            count[s[left]] -= 1
            left += 1

        # update the best
        best = max(best, right - left + 1)

    return best

s = "AABABBA"
res = longestRepCharRep(s, 1)
print(res)
