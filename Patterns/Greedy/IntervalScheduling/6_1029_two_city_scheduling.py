"""
leetcode 1029: Two City Scheduling

Question:
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.
Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Example 1:
Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.
"""

def twoCityScheduling(costs):
    # sort costs by the difference between the two costs in ascending order
    costs.sort(key=lambda x: x[0] - x[1])
    # init cost
    cost = 0
    # traverse costs
    for i in range(len(costs)):
        if i < len(costs) / 2:
            cost += costs[i][0]
        else:
            cost += costs[i][1]
    return cost

print(twoCityScheduling([[10,20],[30,200],[400,50],[30,20]]))
print(twoCityScheduling([[10,20],[30,200],[400,50],[30,20]]))
print(twoCityScheduling([[10,20],[30,200],[400,50],[30,20]]))