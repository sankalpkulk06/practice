"""
Leetcode 1137. Tribonacci Number

The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""

class Solution:
    def tribonacci(self, n):
        """
        Memoization approach:
        - init memo

        base cases:
        - if n == 0, return 0
        - if n = 1 or 2, return 1

        recursive sub problems:
        - Tn = Tn-1 + Tn-2 + Tn-3
        - return the result

        before returning, store the result in memo[n]
        """

        # init memo
        memo = {}

        # helper function
        def soln(n):
            if n in memo:
                return memo[n]

            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1

            memo[n] = soln(n-1) + soln(n-2) + soln(n-3)
            return memo[n]

        return soln(n)
        
if __name__ == "__main__":
    print(Solution().tribonacci(0)) # 0
    print(Solution().tribonacci(1)) # 1
    print(Solution().tribonacci(2)) # 1
    print(Solution().tribonacci(3)) # 2
    print(Solution().tribonacci(4)) # 4
    print(Solution().tribonacci(5)) # 7
    print(Solution().tribonacci(6)) # 13
    print(Solution().tribonacci(7)) # 24
    print(Solution().tribonacci(8)) # 44
    print(Solution().tribonacci(9)) # 81
    print(Solution().tribonacci(10)) # 149