"""
leetcode 1710: Maximum Units on a Truck

Question:
You are assigned to a truck. You are given a list of boxes, each box is represented by a pair of integers (weight, unitsPerBox), where weight is the weight of the box and unitsPerBox is the number of units in each box. You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose to put boxes in any order, and you can take multiple boxes of the same type.

Return the maximum total number of units that can be put on the truck.

Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are three boxes with units 1, 2, and 3. You can take all the boxes for a total of 2 + 4 + 3 = 9 units.

"""

def maxUnits(boxTypes, truckSize):
    # sort boxTypes by unitsPerBox in descending order
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    # init units
    units = 0
    # traverse boxTypes
    for boxType in boxTypes:
        if truckSize >= boxType[0]:
            units += boxType[0] * boxType[1]
            truckSize -= boxType[0]
        else:
            units += truckSize * boxType[1]
            break
    return units

print(maxUnits([[1,3],[2,2],[3,1]], 4))
print(maxUnits([[1,3],[2,2],[3,1]], 3))
print(maxUnits([[1,3],[2,2],[3,1]], 2))
print(maxUnits([[1,3],[2,2],[3,1]], 1))
print(maxUnits([[1,3],[2,2],[3,1]], 0))
print(maxUnits([[1,3],[2,2],[3,1]], 10))
print(maxUnits([[1,3],[2,2],[3,1]], 100))
print(maxUnits([[1,3],[2,2],[3,1]], 1000))
print(maxUnits([[1,3],[2,2],[3,1]], 10000))
print(maxUnits([[1,3],[2,2],[3,1]], 100000))