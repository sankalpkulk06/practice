"""
Leetcode 1482: Minimum Number of Days to Make m Bouquets

Question:
You are given an integer array bloomDay, an integer m, and an integer k. You want to make m bouquets.

To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

Example 1:
Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
Output: 3
"""

"""
---------------------------- Thought Process ----------------------------

ask: can i do in day X?
lower bound = min(bloomDay)
upper bound = max(bloomDay)
do binary search over [min(bloomDay), max(bloomDay)]
"""

def minDays(bloomDay, m, k):
    def can_make(days):
        total_bouq = 0
        consecutive_bloomed = 0

        for i in range(len(bloomDay)):
            if bloomDay[i] <= days:
                consecutive_bloomed += 1
            else:
                # not bloomed, seq is broken
                consecutive_bloomed = 0
            
            # if we have enough adj bloomed
            if consecutive_bloomed == k:
                total_bouq += 1
                consecutive_bloomed = 0 #reset
        
        return total_bouq >= m

    if m * k > len(bloomDay):
        return -1

    # init
    L = min(bloomDay)
    R = max(bloomDay)
    res = max(bloomDay)

    while L <= R:
        mid = (L + R) // 2

        if can_make(mid):
            # day that works, lets check if there is a day that is better
            res = mid
            R = mid - 1
        else:
            # too soon
            L = mid + 1
    return res


print(minDays([1,10,3,10,2], 3, 1))
print(minDays([1,10,3,10,2], 3, 2))
print(minDays([1,10,3,10,2], 3, 3))