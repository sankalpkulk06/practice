"""

Write a function `canSum(targetSum, numbers)` that takes in a target sum and an array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to generate the target sum using the numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are non-negative.
"""



def canSum_naive(targetSum, numbers):
    """
    Naive approach:

    Base cases:
    - if target sum is 0, return True
    - if target sum is negative, return False
    - if numbers is empty, return False
    - otherwise, return the result of the subproblems

    Recursive approach:
    - for all the numbers in the array, we find the shrunk target
    - if the shrunk target is a solution, return True
    - otherwise, return False
    """
    
    # base case
    if targetSum == 0:  # solution found
        return True
    if targetSum < 0:  # solution not found
        return False
    if not numbers:  # no numbers to use
        return False
    
    # recursive 
    # for all the numbers in the array, we find the shrunk target
    for num in numbers:
        remainder = targetSum - num
        if canSum_naive(remainder, numbers):
            return True
    
    # solution not found
    return False

def canSum_memoization(targetSum, numbers, memo=None):
    """
    Memoization approach:

    - use a dictionary to store the results of the can sum
    - if the result is already in the memo, return it
    - otherwise, calculate the result and store it in the memo and then return it
    """

    if memo is None:
        memo = {}
    
    # base cases
    if targetSum == 0:  # solution found
        return True
    if targetSum < 0:  # solution not found
        return False

    # check if the result is already in the memo, then return it
    if targetSum in memo:
        return memo[targetSum]
    
    # recursive 
    # for all the numbers in the array, we find the shrunk target
    for num in numbers:
        remainder = targetSum - num
        
        # calculate the result and store it in the memo and then return it
        if canSum_memoization(remainder, numbers, memo):
            memo[targetSum] = True
            return True
    
    # solution not found
    memo[targetSum] = False
    return False

if __name__ == "__main__":
    print(canSum_naive(7, [2, 3]))
    print(canSum_naive(7, [5, 3, 4, 7]))
    print(canSum_naive(7, [2, 4]))
    print(canSum_naive(8, [2, 3, 5]))
    # print(canSum_naive(300, [7, 14])) # this will take a long time to compute
    print(canSum_memoization(7, [2, 3]))
    print(canSum_memoization(7, [5, 3, 4, 7]))
    print(canSum_memoization(7, [2, 4]))
    print(canSum_memoization(8, [2, 3, 5]))
    print(canSum_memoization(300, [7, 14]))