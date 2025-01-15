"""
168. Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
"""

def convertToTitle(columnNumber):
    result = ''

    while columnNumber > 0:
        columnNumber -= 1

        currChar = chr(columnNumber % 26 + ord('A'))

        result = currChar + result

        columnNumber //= 26

    return result

print(convertToTitle(28))