"""
LC 1461: Check If a String Contains All Binary Codes of Size K

Question:
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

 
Example 1:

Input: s = "00110110", k = 2
Output: true

"""

def hasAllCodes(s, k):
    # init
    need = 2 ** k
    seen = set()

    # check impossible case
    if len(s) < need:
        return False
    if len(s) - k + 1 < need:
        return False
    
    # slide window
    for i in range(len(s) - k + 1):
        # print(s[i:i+k])
        code = s[i : i+k]
        seen.add(code)

        # early exit - check if we have seen all codes
        if len(seen) == need:
            return True
    return False

print(hasAllCodes("00110110", 2))
print(hasAllCodes("0110", 2))
print(hasAllCodes("0110", 1))
print(hasAllCodes("0110", 3))
print(hasAllCodes("0110", 4))
print(hasAllCodes("0110", 5))
print(hasAllCodes("0110", 6))
print(hasAllCodes("0110", 7))
print(hasAllCodes("0110", 8))
print(hasAllCodes("0110", 9))
print(hasAllCodes("0110", 10))
