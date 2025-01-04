"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

"""
Logic:

flower
flow
flight

take the smallest word and start matching the indeces of all the words in the list
if there is a mismatch, stop and return the string
"""

def longestCommonPrefix(strs):
    
    if len(strs) == 1:
        print(len(strs), strs)
        return strs[0]

    # get the smallest word
    smallest_len = 999
    for str in strs:
        if len(str) < smallest_len:
            smallest_len = len(str)
        if len(str) == 0:
            return ""

    for i in range(smallest_len):
        for str in strs:
            if str[i] != strs[0][i]:    # compare str[i] with the first string's ith char in the list
                return str[:i]

    return strs[0][:smallest_len]  # if there is no mismatch

print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["ab", "a"]))
print(longestCommonPrefix(["a"]))
