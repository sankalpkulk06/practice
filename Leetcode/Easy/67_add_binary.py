"""
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

"""

def addBinary(a, b):
    return bin(int(str(a),2) + int(str(b),2))[2:]   # [2:] removed the 0b infront of all the bin nums

print(addBinary(100, 1))