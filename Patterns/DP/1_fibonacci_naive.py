"""
Fibonacci Sequence:

Write a function `fib(n)` that takes in a number as an argument,
The function should return the nth number of the Fibonacci sequence

The 1st and 2nd number of the sequence is 1.
To generate the next number of the sequence , we sum the previous two.

n = 1, fib(n) = 1
n = 2, fib(n) = 1
n = 3, fib(n) = 2
n = 4, fib(n) = 3
n = 5, fib(n) = 5
n = 6, fib(n) = 8
n = 7, fib(n) = 13
n = 8, fib(n) = 21
n = 9, fib(n) = 34
n = 10, fib(n) = 55
"""

def fib(n):

    # since fib(1) and fib(2) are 1, we can return 1 for both
    if n <= 2:
        return 1
    
    # recursive approach
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    print(fib(6))
    print(fib(7))
    print(fib(10))

    print(fib(50))