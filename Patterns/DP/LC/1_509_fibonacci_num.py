"""
Leetcode 509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.

Given n, calculate F(n).
"""

class Solution:
    def fib(self, n: int) -> int:
        """
        Memoization approach:
        - use a dictionary to store the results of the fibonacci sequence
        - if the result is already in the memo, return it
        - otherwise, calculate the result and store it in the memo and then return it
        """
        # helper function
        def fibonacci(n, memo={}):
            if n in memo:
                return memo[n]
            if n <= 1:
                return n
            memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
            return memo[n]

        return fibonacci(n, {})


if __name__ == "__main__":
    print(Solution().fib(2)) # 1
    print(Solution().fib(3)) # 2
    print(Solution().fib(4)) # 3
    print(Solution().fib(5)) # 5
    print(Solution().fib(6)) # 8
    print(Solution().fib(7)) # 13
    print(Solution().fib(8)) # 21
    print(Solution().fib(9)) # 34
    print(Solution().fib(10)) # 55