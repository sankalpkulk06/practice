"""
Problem Statement
canConstruct(target, wordBank)

Input: 
A target string (string) and an array of strings (wordBank).

Output: 
A boolean indicating whether or not the target can be constructed by concatenating elements of the wordBank array.

Constraint: 
You may use elements of the wordBank array as many times as needed.

Example 1:
Input: target = "abcdef", wordBank = ["ab", "abc", "cd", "def", "abcd"]
Output: true

Example 2:
Input: target = "skateboard", wordBank = ["bo", "rd", "ate", "t", "ska", "sk", "boar"]
Output: false

Example 3:
Input: target = "enterapotentpot", wordBank = ["a", "p", "ent", "enter", "ot", "o", "t"]
"""

def canConstruct_naive(target, wordBank):
    """
    Brute Force Approach:

    base cases:
    - if target is empty, return True
    - if wordBank is empty, return False

    recurive subproblems:
    - for each word in wordBank,
        - if the word is a prefix of target,
            - recursively call canConstruct with remaining of target after removing the word
            - if that call returns True, return True
        - otherwise, return False
    - if no word in wordBank is a prefix of target, return False
    """

    # base case
    if target == "":
        return True
    if not wordBank:
        return False

    # helper function
    # check if word is a prefix of target
    def is_prefix(word, target):
        return target.startswith(word)
    
    # recurive subproblems
    for word in wordBank:

        # check if the word is a prefix of target
        if is_prefix(word, target):
            remainingTarget = target[len(word) : ]

            # check if the remaining target can be constructed
            if canConstruct_naive(remainingTarget, wordBank):
                return True
    
    # solution not found
    return False


def canConstruct_memoization(target, wordBank, memo=None):
    """
    Memoization approach:

    base cases:
    - if target is empty, return True
    - if wordBank is empty, return False
    - if the result is already in the memo, return it

    recurive subproblems:
    - for each word in wordBank,
        - if the word is a prefix of target,
            - recursively call canConstruct with remaining of target after removing the word
            - if that call returns True, return True
        - otherwise, return False
    - if no word in wordBank is a prefix of target, return False
    """

    # memoization
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]

    # base case
    if target == "":
        memo[target] = True
        return True
    if not wordBank:
        memo[target] = False
        return False

    # helper function
    # check if word is a prefix of target
    def is_prefix(word, target):
        return target.startswith(word)
    
    # recurive subproblems
    for word in wordBank:

        # check if the word is a prefix of target
        if is_prefix(word, target):
            remainingTarget = target[len(word) : ]

            # check if the remaining target can be constructed
            if canConstruct_memoization(remainingTarget, wordBank, memo):
                memo[target] = True
                return True
    
    # solution not found
    memo[target] = False
    return False

if __name__ == "__main__":
    print(canConstruct_naive("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(canConstruct_naive("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(canConstruct_naive("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    # print(canConstruct_naive("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # this will take a long time to compute
    print(canConstruct_memoization("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(canConstruct_memoization("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
    print(canConstruct_memoization("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
    print(canConstruct_memoization("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  