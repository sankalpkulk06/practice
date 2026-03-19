"""
Write a function `canSum(targetSum, numbers)` that takes in a target sum and an array of numbers as arguments.

The function should return a boolean indicating whether or not it is possible to generate the target sum using the numbers from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are non-negative.
"""

def canSum(targetSum, numbers):
    """
    Tabulation (bottom-up) approach:

    init:
    - init a table with targetSum+1 elements
    - initialize all elements to False

    base cases:
    - since index 0 is the target sum, we set table[0] to True (pick 0 elements from the array, always true)

    fill the table:
    - iterate through the table:
        - for each element, 
        check if it is a solution (is True)
        if it is a solution, look that many steps ahead and set the next index to True
        if it is not a solution, skip
    - return the targetSum index in the table
    """
    
    # init table
    table = [False] * (targetSum + 1)

    # base cases
    table[0] = True
    # print(table)

    # fill the table
    for i in range(len(table)):
        # check if that index is a solution (is True)
        if table[i]:
            for num in numbers:
                # look that many steps ahead
                if i + num <= targetSum:
                    table[i+num] = True

    return table[targetSum]

if __name__ == "__main__":
    print(canSum(7, [2, 3]))
    print(canSum(7, [5, 3, 4, 7]))
    print(canSum(7, [2, 4]))
    print(canSum(8, [2, 3, 5]))
    print(canSum(300, [7, 14]))