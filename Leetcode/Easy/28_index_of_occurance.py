"""
28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""

def strStr(haystack, needle):

    if not needle:
        return 0
    
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:len(needle) + i] == needle:
            return i
    return -1

print(strStr("leetcode", "leet"))
print(strStr("sadbutsad", "but"))

# def strStr(haystack, needle):
    
#     flag = False
#     index = -1
#     for i in range(len(haystack) - len(needle)):
#         if haystack[i] == needle[i]:
#             for j in range(1, len(needle)):
#                 if haystack[i] == needle[i]:
#                     flag = True
#                 else:
#                     flag = False
#             if flag == True:
#                 index = i
#                 return index
            
#     return index
    

