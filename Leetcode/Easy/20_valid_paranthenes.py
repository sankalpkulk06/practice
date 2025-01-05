"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false
"""

"""
Logic:
- first thoughts: use a stack

for example, ({})
Stack 
1. top ( |bottom, push (
2. top {( |bottom, push {
3. top }{( |bottom, pop }, pop {
4. top )( |bottom, pop, pop

"""

def isValid(str):

    stack = []
    mapping = {
        "]": "[",
        "}": "{",
        ")": "("
    }

    for char in str:
        if char in mapping:
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return not stack

print(isValid("(){}"))
print(isValid("()}"))
print(isValid("({})"))
print(isValid("((({[]})))"))