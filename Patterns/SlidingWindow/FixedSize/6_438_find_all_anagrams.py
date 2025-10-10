"""
LeetCode 438: Find All Anagrams in a String

Question:
Given two strings s and p, return an array of all the start indices of p's anagrams in s.

Example:    
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

"""

from collections import defaultdict
from typing import List

def findAnagrams(s: str, p: str) -> List[int]:
    
    # init
    n, m = len(s), len(p)
    if m > n:
        return []

    # init need and window
    need = defaultdict(int)
    window = defaultdict(int)

    # init need
    for ch in p:
        need[ch] += 1
    
    # init window
    for i in range(m):
        window[s[i]] += 1

    # check if the first window is an anagram
    res = []
    if window == need:
        res.append(0)

    # slide window: i is the index of the incoming char
    for i in range(m, n):
        window[s[i]] += 1   # add the incoming char
        window[s[i-m]] -= 1 # remove the outgoing char

        if window[s[i-m]] == 0:
            del window[s[i-m]]
        
        if window == need:
            res.append(i-m+1) # add the start index of the anagram
    return res

s = "cbaebabacd"
p = "abc"
res= findAnagrams(s, p)
print(res)

s = "abab"
p = "ab"
res = findAnagrams(s, p)
print(res)