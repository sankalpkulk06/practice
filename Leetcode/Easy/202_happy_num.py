"""
202. Happy Number

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false

"""

def isHappy(n: int) -> bool:
    
    # Two-Pointer Pattern

    # Helper function to get the sum of squares of digits
    def get_next(num):
        total_sum = 0
        while num > 0:
            digit = num % 10
            total_sum += digit * digit
            num //= 10
        return total_sum
    
    slow = n
    fast = get_next(n)

    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1

print(isHappy(2))
print(isHappy(19))