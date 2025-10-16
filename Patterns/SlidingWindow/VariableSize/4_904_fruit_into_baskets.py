"""
LeetCode 904: Fruit Into Baskets

Question:
You are visiting a farm that has a single row of fruit trees arranged from left to right. 
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
You want to pick the maximum number of fruits. However, you can only pick at most two types of fruit.

You start at any tree of your choice, then traverse the row of trees from left to right, picking every fruit you see. You can only pick one type of fruit at a time.

You can start with any tree, but once you have started picking fruit from a tree, you cannot skip the next tree. 
You will pick exactly one fruit from each tree until you cannot, i.e., you will stop when you have to pick a third type of fruit.

Given the integer array fruits, return the maximum number of fruits you can pick.

Example:
Input: fruits = [1,2,1]
Output: 3

"""
from collections import defaultdict

def maxFruit(fruits: list[int]) -> int:
    # init pointers
    left = 0
    best = 0
    count = defaultdict(int)
    
    # slide the window
    for right in range(len(fruits)):
        # expand the window
        count[fruits[right]] += 1

        # shrink the window (INVALID)
        while len(count) > 2:
            count[fruits[left]] -= 1
            if count[fruits[left]] == 0:
                del count[fruits[left]]
            left += 1

        # update the best
        best = max(best, right - left + 1)

    return best 

fruits = [1,2,1]
res = maxFruit(fruits)
print(res)

print(maxFruit([3,3,3,1,2,1,1,2,3,3,4]))

print(maxFruit([1,2,3,2,2]))