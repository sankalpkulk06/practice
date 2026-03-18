"""

Write a function `gridTraveler(m, n)` that takes in a number of rows and columns and returns the number of ways to travel from the top-left to the bottom-right of a grid.

You can only move down or right.

Example 1:
Input: m = 2, n = 3
Output: 3

Example 2:
Input: m = 3, n = 2
Output: 3
"""


def gridTraveler_naive(m, n):
    """
    Naive approach:

    - no memoization
    - consider base cases:
        - if m or n is 0, return 0
        - if m or n is 1, return 1
    - otherwise, return the sum of the ways to travel the grid from the top-left to the bottom-right
    """
    
    # base cases
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    
    # recursive approach: sum of the ways to travel the grid from the top-left to the bottom-right
    return gridTraveler_naive(m-1, n) + gridTraveler_naive(m, n-1)

def gridTraveler_memoization(m, n, memo={}):
    """
    Memoization approach:

    - use a dictionary to store the results of the grid traveler
    - if the result is already in the memo, return it
    - otherwise, calculate the result and store it in the memo and then return it
    """
    
    # base cases
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    
    # check if the result is already in the memo, then return it
    if (m, n) in memo:
        return memo[(m, n)]
    
    memo[(m, n)] = gridTraveler_memoization(m-1, n, memo) + gridTraveler_memoization(m, n-1, memo)
    return memo[(m, n)]

if __name__ == "__main__":
    print(gridTraveler_naive(2, 3))
    print(gridTraveler_naive(3, 2))
    print(gridTraveler_naive(3, 3))
    # print(gridTraveler_naive(18, 18)) # this will take a long time to compute
    print(gridTraveler_memoization(2, 3))
    print(gridTraveler_memoization(3, 2))
    print(gridTraveler_memoization(3, 3))
    print(gridTraveler_memoization(18, 18))