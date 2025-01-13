"""
125. Valid Palindrome
"""

def isPalindrome(s):
    s = s.lower()

    filtered_str = [char for char in s if char.isalnum()]

    for i in range(len(s)//2):
        # print(s[i])
        if filtered_str[i] != filtered_str[len(filtered_str)-1-i]:
            return False
    return True

print(isPalindrome("A man, a plan, a canal: Panama"))