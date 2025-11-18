"""
Leetcode 1883: Maximum Ice Cream Bars

Question:
You are given an integer array costs where costs[i] is the cost of the ith ice cream bar in a shop. 
You are also given an integer coins which represents the number of dollars you have in your pocket.

You want to maximize the number of ice cream bars you can eat and return the maximum number of ice cream bars you can eat.

Example 1:
Input: costs = [1,3,2,4,1], coins = 7
Output: 4
Explanation: The boy can buy ice cream bars at indices 0, 1, 2, 4 for a total price of 1 + 3 + 2 + 1 = 7.
"""

def maxIceCream(costs, coins):
    # sort the costs array
    costs.sort()
    # init the number of ice cream bars
    max_bars = 0
    # traverse the costs array
    for cost in costs:
        if coins >= cost:
            coins = coins - cost
            max_bars += 1
        else:
            break
    return max_bars

print(maxIceCream([1,3,2,4,1], 7))
print(maxIceCream([10,6,8,7,7,8], 5))