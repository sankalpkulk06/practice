"""
Problem Statement
howSum(targetSum, numbers)

Input: 
A targetSum (integer) and an array of numbers (integers, non-negative).

Output: 
An array containing any combination of elements that add up to exactly the targetSum. If no combination exists, return null (or equivalent, such as an empty array in some implementations).

Constraint: 
You can use elements from the numbers array as many times as needed. 

Example 1:
Input: targetSum = 7, numbers = [2, 3]
Output: [3, 2, 2]

Example 2:
Input: targetSum = 7, numbers = [5, 3, 4, 7]
Output: [7]

"""


def howSum_naive(targetSum, numbers):
    """
    Naive approach:

    Base cases:
    - if target sum is 0, return []
    - if target sum is negative, return False
    - if numbers is empty, return False
    - otherwise, return the result of the subproblems

    Recursive approach:
    - for all the numbers in the array, we find the shrunk target
    - if the shrunk target is a solution, return the solution
    - otherwise, return None
    """
    
    # base case
    if targetSum == 0:  # solution found
        return []
    if targetSum < 0:  # solution not found
        return None
    

    # recursive
    for num in numbers:
        remainder = targetSum - num

        remianderResult = howSum_naive(remainder, numbers)

        # if found a valid combination
        if remianderResult is not None:
            return remianderResult + [num]

    # solution not found
    return None

def howSum_memoization(targetSum, numbers, memo=None):
    """
    Memoization approach:

    - use a dictionary to store the results of the how sum with the target sum as the key
    - if the result is already in the memo, return it
    """

    # memoization: base cases
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    
    # base cases
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    # recursive
    for num in numbers:
        remainder = targetSum - num

        # store the result in memo
        remainderResult = howSum_memoization(remainder, numbers, memo)

        if remainderResult is not None:
            memo[targetSum] = remainderResult + [num]
            return memo[targetSum]

    # solution not found
    memo[targetSum] = None
    return None
    

if __name__ == "__main__":
    print(howSum_naive(7, [2, 3]))
    print(howSum_naive(7, [5, 3, 4, 7]))
    print(howSum_naive(7, [2, 4]))
    print(howSum_naive(8, [2, 3, 5]))
    # print(howSum_naive(300, [7, 14])) # this will take a long time to compute
    print(howSum_memoization(7, [2, 3]))
    print(howSum_memoization(7, [5, 3, 4, 7]))
    print(howSum_memoization(7, [2, 4]))
    print(howSum_memoization(8, [2, 3, 5]))
    print(howSum_memoization(300, [7, 14])) 