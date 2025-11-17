"""
leetcode 1217: Minimum Cost to Move Chips to The Same Position

Question:
You are given an integer array position where position[i] represents the position of the ith chip. You can move the ith chip by 1 unit to the left or right with a cost of 1. You can move the ith chip by 2 units to the left or right with a cost of 0.

Return the minimum cost to move all the chips to the same position.

Example 1:
Input: position = [1,2,3]
Output: 1
Explanation: The first chip is already at the position 2, the second chip is at position 3, and the third chip is at position 1. The first chip needs to be moved to the position 2 to make the positions equal. The second chip needs to be moved to the position 2 to make the positions equal. The third chip needs to be moved to the position 2 to make the positions equal. The total cost is 1.

Example 2:
Input: position = [2,2,2,3,3]
Output: 2
Explanation: The first two chips are already at the position 2, the third chip is at position 3, and the fourth and fifth chips are at position 3. The first two chips need to be moved to the position 2 to make the positions equal. The third chip needs to be moved to the position 2 to make the positions equal. The fourth and fifth chips need to be moved to the position 2 to make the positions equal. The total cost is 2.

"""

def minCostToMoveChips(position):
    count_even = sum(p % 2 == 0 for p in position)
    count_odd = len(position) - count_even

    return min(count_even, count_odd)

print(minCostToMoveChips([1,2,3]))
print(minCostToMoveChips([2,2,2,3,3]))
print(minCostToMoveChips([1,1000000000]))
print(minCostToMoveChips([1,1000000000,1000000000]))