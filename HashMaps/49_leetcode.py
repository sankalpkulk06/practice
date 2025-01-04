"""
49. Group Anagrams (MEDIUM)

Given an array of strings strs, group the anagrams togeather. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the org letters exactly once.

Example 1:
    Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["bat], ["nat", "tan"], ["ate", "eat", "tea"]]

def groupAnagrams(strs: List[str]) -> List[List[str]]:
"""
from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)
    result = []

    for word in strs:
        # sort all the letters and use that as a key for the anagram_map
        # sorted_word is still mutalale so we make it into a tuple
        sorted_word = tuple(sorted(word))

        # sorted_word is still mutalale so we make it into a tuple
        anagram_map[sorted_word].append(word)

    # print(anagram_map)

    for value in anagram_map.values():
        result.append(value)

    return result

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = groupAnagrams(strs)
print(output)