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

def gridTraveler(m, n):
    """
    Tabulation approach:

    Base cases:
    - we know gridTraveler(0, 0) = 0 
    - we know gridTraveler(1, 1) = 1

    Fill the table:
    - iterate through each cell in the table (row wise)
    - for each cell, add the number of ways to travel to the cell from the left and the cell from the top
    - return the last cell in the table
    """
    
    # init table
    table = [[0] * (n+1) for _ in range(m+1)]
    # print(table)

    # base cases
    if m == 0 or n == 0:
        return 0
    table[1][1] = 1
    

    # fill the table
    for i in range(m+1):
        for j in range(n+1):
            # take the current cell and add the number to the right cell and down cell
            if i + 1 <= m:
                table[i+1][j] += table[i][j]
            if j + 1 <= n:
                table[i][j+1] += table[i][j]
    # print(table)

    return table[m][n]

if __name__ == "__main__":
    print(gridTraveler(1, 1))
    print(gridTraveler(0, 0))
    print(gridTraveler(0, 1))
    print(gridTraveler(1, 0))
    print(gridTraveler(2, 3))
    print(gridTraveler(3, 2))
    print(gridTraveler(3, 3))
    print(gridTraveler(18, 18))