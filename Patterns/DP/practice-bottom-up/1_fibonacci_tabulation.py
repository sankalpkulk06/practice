"""
Write a function `fib(n)` that takes in a number and returns the nth number in the Fibonacci sequence.

The 0th number in the sequence is 0.
The 1st number in the sequence is 1.

To generate the next number in the sequence, we sum the previous two.

n: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
fib(n): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
"""

def fib(n):
    """
    Tabulation approach:
    - init a table with n+1 elements

    """

    # init table
    table = [0] * (n+1)
    # print(table)

    # base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        table[1] = 1

    # fill the table
    for i in range(n):
        if i + 1 <= n:
            table[i+1] += table[i]
        if i + 2 <= n:
            table[i+2] += table[i]

    return table[n]

if __name__ == "__main__":
    print(fib(0))
    print(fib(1))
    print(fib(2))
    print(fib(3))
    print(fib(4))
    print(fib(5))
    print(fib(6))
    print(fib(7))
    print(fib(8))
    print(fib(9))
    print(fib(100))