"""

Problem Statement
allConstruct(target, wordBank)

Input: 
A target string (string) and an array of strings (wordBank).

Output: 
An array of arrays containing all the ways that the target can be constructed by concatenating elements of the wordBank array.

Constraint: 
You may use elements of the wordBank array as many times as needed.

Example 1:
Input: target = "abcdef", wordBank = ["ab", "abc", "cd", "def", "abcd"]
Output: [["ab", "cd", "ef"], ["ab", "c", "def"], ["abc", "def"], ["abcd", "ef"]]

Example 2:
Input: target = "skateboard", wordBank = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
Output: []

Example 3:
Input: target = "enterapotentpot", wordBank = ["a", "p", "ent", "enter", "ot", "o", "t"]
"""

def allConstruct_naive(target, wordBank):
    """
    Brute Force Approach:

    base cases:
    - if target is empty, return [[]]
    - if wordBank is empty, return []

    recurive sub problems:
    - for each word in wordBank,
        - if the word is a prefix of target,
            - recursively call allConstruct with remaining of target after removing the word
            - all the results are combined and returned
        - otherwise, return []
    - if no word in wordBank is a prefix of target, return []
    """

    # base cases
    if target == "":
        return [[]]
    if not wordBank:
        return []

    # helper function
    # check if word is a prefix of target
    def is_prefix(word, target):
        return target.startswith(word)
    
    # init
    allWays = []

    # recurive sub problems
    for word in wordBank:
        # check if the word is a prefix of target
        if is_prefix(word, target):

            suffix = target[len(word) : ]
            suffixWays = allConstruct_naive(suffix, wordBank)

            #  add the word to the suffix ways in front
            targetWays = [ [word] + way for way in suffixWays ]

            allWays.extend(targetWays)

    # return the all ways
    return allWays

def allConstruct_memoization(target, wordBank, memo=None):
    """
    Memoization approach:

    base cases:
    - if target is empty, return [[]]
    - if wordBank is empty, return []
    - if the result is already in the memo, return it

    recurive sub problems:
    - for each word in wordBank,
        - if the word is a prefix of target,
            - recursively call allConstruct with remaining of target after removing the word
            - all the results are combined and returned
        - otherwise, return []
    - if no word in wordBank is a prefix of target, return []
    - store the result in the memo
    """
    # memoization
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    # base cases
    if target == "":
        return [[]]
    if not wordBank:
        return []

    # helper function
    # check if word is a prefix of target
    def is_prefix(word, target):
        return target.startswith(word)

    # init
    allWays = []

    # recurive sub problems
    for word in wordBank:
        # check if the word is a prefix of target
        if is_prefix(word, target):

            suffix = target[len(word) : ]
            suffixWays = allConstruct_memoization(suffix, wordBank, memo)

            #  add the word to the suffix ways in front
            targetWays = [ [word] + way for way in suffixWays ]

            allWays.extend(targetWays)

    # return the all ways
    memo[target] = allWays
    return allWays


if __name__ == "__main__":
    print(allConstruct_naive("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(allConstruct_naive("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(allConstruct_naive("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    # print(allConstruct_naive("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))    # this will take a long time to compute
    print(allConstruct_memoization("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(allConstruct_memoization("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(allConstruct_memoization("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(allConstruct_memoization("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))