"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

"""
Logic:
- The problem is similar to the Fibonacci sequence
"""

def climbStairs(n):
    
    if n <= 2:
        return n
    
    prev1, prev2 = 2, 1
    for _ in range(3, n+1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1

print(climbStairs(4))