"""
leetcode 135: Candy

Question:
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

"""

def candy(ratings):
    # init candies
    candies = [1] * len(ratings)
    # traverse the ratings from left to right
    for i in range(1, len(ratings)):
        # [1, 1, 2]
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    # traverse the ratings from right to left
    for i in range(len(ratings) - 2, -1, -1):
        # [1, 2, 1]
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    return sum(candies)

print(candy([1,0,2]))
print(candy([1,2,2]))
print(candy([1,2,3,4,5]))
print(candy([5,4,3,2,1]))
print(candy([1,2,3,4,5,6,7,8,9,10]))
print(candy([10,9,8,7,6,5,4,3,2,1]))
print(candy([1,2,3,4,5,6,7,8,9,10]))