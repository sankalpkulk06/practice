"""
Leetcode 875: Koko Eating Bananas

Question:
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

"""

"""
---------------------------- Thought Process ----------------------------

Given to us is that LENGTH OF PILES <= H, so we can use this to our advantage. Otherwise Koko wont be able to finish eating all the bananas.

lets take an example:
piles = [3,6,7,11]
h = 8

now its easy to see that Koko can eat all the bananas in 8 hours if she eats 4 bananas per hour.

now what is the lower bound?
- lower bound is 1, because Koko has to eat at least 1 banana per hour.

now what is the upper bound?
- upper bound is the max(piles), because Koko can eat at most the max(piles) bananas per hour.

so our search space is [1, 11].

-- Brute Force Approach:
K = 1
	- 3/1 = 3 hours to eat this pile
	- 6/1 = 6 hours to eat this pile
K = 2
3/2 = 2 hours to eat this pile
the complexity of this approach is O(n^2), because we are trying all the possible capacities

Search Space: [1, 11]

-- Binary Search Approach:
L = 1
R = max(piles) = 11

mid = 6
    - 3/6 = 1 hour to eat this pile
    - 6/6 = 1 hour to eat this pile
    - 7/6 = 2 hours to eat this pile
    - 11/6 = 2 hours to eat this pile
    - total hours = 6 hours < 8 -> valid
    - is there a better speed?
    - R = mid - 1 = 5
mid = 3
    - 1 + 2 + 3 + 4 = 10 hours > 8 -> not valid
    - L = mid + 1 = 4
mid = 4
    - 1+2+2+3 = 8 hours == 8 -> valid
"""

def minEatingSpeed(piles, h):
    
    def can_eat(k):
        # hours taken to eat all the piles speed k
        hr = 0
        for p in piles:
            hr += p // k
            if p % k != 0:
                hr += 1
            """
            or we can use the ceil function
            hr += math.ceil(p / k)
            """
        return hr <= h
    # init
    L = 1   # lower bound   
    R = max(piles) # upper bound
    result = R # result

    while L <= R:
        mid = (L + R) // 2
        if can_eat(mid):
            result = min(result, mid)
            R = mid - 1
        else:
            L = mid + 1
    return result

print(minEatingSpeed([3,6,7,11], 8))
print(minEatingSpeed([30,11,23,4,20], 5))
print(minEatingSpeed([30,11,23,4,20], 6))