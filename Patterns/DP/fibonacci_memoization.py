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


Memoization:
- we will use a dictionary to store the results of the fibonacci sequence
- whenever we calculate a fibonacci number, we will store the result in the dictionary
"""

def fib(n, memo={}):
    # check if the result is already in the memo, then return it
    if n in memo:
        return memo[n]

    # if n in 1 or 2, return 1
    if n <= 2:
        return 1
    
    # if n is not in the memo, calculate the result and store it in the memo and then return it
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
    

if __name__ == "__main__":
    print(fib(6))
    print(fib(7))
    print(fib(10))
    print(fib(50))