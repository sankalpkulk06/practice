"""
LeetCode 1876: Substrings of Size Three with Distinct Characters

Question:
A string is good if there are no repeated characters.
Given a string s, return the number of good substrings of length three in s.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

Example:
Input: s = "xyzzaz"
Output: 1
"""
from collections import defaultdict

def countGoodSubstrings(s: str) -> int:

    if len(s) < 3:
        return 0
    # init
    k = 3
    freq = defaultdict(int)
    dup = 0

    # init window
    for ch in s[:k]:
        freq[ch] += 1
        if freq[ch] == 2:
            dup += 1
    
    ans = 0
    if dup == 0:
        ans += 1
    
    # slide the window
    for i in range(k, len(s)):

        right_ch = s[i]
        left_ch = s[i-k]

        # incoming
        freq[right_ch] += 1
        if freq[right_ch] == 2:
            dup += 1
        
        # outgoing
        freq[left_ch] -= 1
        if freq[left_ch] == 1:
            dup -= 1
        
        elif freq[left_ch] == 0:
            del freq[left_ch]

        if dup == 0:
            ans += 1

    return ans       


s = "xyzzaz"
res = countGoodSubstrings(s)
print(res)