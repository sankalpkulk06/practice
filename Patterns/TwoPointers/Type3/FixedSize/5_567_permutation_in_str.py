"""
LeetCode 567: Permutation in String

Question:
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true

"""

from collections import defaultdict

def checkInclusion(s1: str, s2: str) -> bool:

    # init
    n, m = len(s1), len(s2)
    if n > m: 
        return False

    need = defaultdict(int)
    window = defaultdict(int)
    
    for ch in s1:
        need[ch] += 1
    
    # init window
    for i in range(n):
        window[s2[i]] += 1
    
    if window == need:
        return True
    
    for i in range(n, m):
        # incoming
        window[s2[i]] += 1
        # outgoing
        window[s2[i-n]] -= 1

        # remove 0 values
        if window[s2[i-n]] == 0:
            del window[s2[i-n]]

        if window == need:
            return True
    
    return False

s1 = "ab"
s2 = "eidbaooo"
res = checkInclusion(s1, s2)
print(res)

s1 = "ab"
s2 = "eidboaoo"
res = checkInclusion(s1, s2)
print(res)


s1 = "adc"
s2 = "dcda"
res = checkInclusion(s1, s2)
print(res)

