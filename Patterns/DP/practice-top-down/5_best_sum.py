"""

Problem Statement
bestSum(targetSum, numbers)

Input: 
A targetSum (integer) and an array of numbers (integers, non-negative).

Output: 
An array containing the shortest combination of numbers that add up to exactly the targetSum. If no combination exists, return null (or equivalent, such as an empty array in some implementations).

Constraint: 
You can use elements from the numbers array as many times as needed. 

Example 1:
Input: targetSum = 7, numbers = [5, 3, 4, 7]
Output: [7]

Example 2:
Input: targetSum = 8, numbers = [2, 3, 5]
Output: [3, 5]

"""

def bestSum_naive(targetSum, numbers):
    """
    Naive approach:

    Base cases:
    - if target sum is 0, return []
    - if target sum is negative, return None
    - otherwise, return the result of the subproblems
    
    Recursive approach:
    - for all the numbers in the array, we find the shrunk target
    - if the shrunk target is a solution, update the shortest combination
    - otherwise, return None
    """
    
    # base cases
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    # init
    shortestCombination = None
    
    # branching logic (recursive):
    for num in numbers:
        remainder = targetSum - num

        remianderCombination = bestSum_naive(remainder, numbers)

        # if found a valid combination
        if remianderCombination is not None:
            # update the combination
            combination = remianderCombination + [num]

            # if the combination is shorter than the current "shortest", update it
            if ( shortestCombination is None ) or ( len(combination) < len(shortestCombination) ):
                shortestCombination = combination

    # return the shortest combination
    return shortestCombination

def bestSum_memoization(targetSum, numbers, memo=None):
    """
    Memoization approach:

    - use a dictionary to store the results of the best sum
    - if the result is already in the memo, return it
    - otherwise, calculate the result and store it in the memo and then return it
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

    # init
    shortestCombination = None
    
    # branching logic (recursive):
    for num in numbers:
        remainder = targetSum - num

        remianderCombination = bestSum_memoization(remainder, numbers, memo)

        # if found a valid combination
        if remianderCombination is not None:
            # update the combination
            combination = remianderCombination + [num]

            # if the combination is shorter than the current "shortest", update it
            if ( shortestCombination is None ) or ( len(combination) < len(shortestCombination) ):
                shortestCombination = combination

    # return the shortest combination
    memo[targetSum] = shortestCombination
    return shortestCombination

if __name__ == "__main__":
    print(bestSum_naive(7, [5, 3, 4, 7]))
    print(bestSum_naive(8, [2, 3, 5]))
    print(bestSum_naive(8, [1, 4, 5]))
    # print(bestSum_naive(300, [7, 14])) # this will take a long time to compute
    print(bestSum_memoization(7, [5, 3, 4, 7]))
    print(bestSum_memoization(8, [2, 3, 5]))
    print(bestSum_memoization(8, [1, 4, 5]))
    print(bestSum_memoization(300, [7, 14])) # this will take a long time to compute