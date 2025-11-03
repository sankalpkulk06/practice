"""
leetcode 452: Minimum Number of Arrows to Burst Balloons

Question:
There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. 
You do not know the exact y-coordinates of the balloons.

A shot arrow can burst all balloons whose horizontal diameter intersects with the balloon. Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""

def minArrows(points):
    # sort points by end time in ascending order
    points.sort(key=lambda x: x[1])
    # init count
    count = 0
    prev_end = -float('inf')
    
    for start, end in points:
        if start > prev_end:
            prev_end = end
            count += 1
    return count

print(minArrows([[10,16],[2,8],[1,6],[7,12]]))
print(minArrows([[1,2],[3,4],[5,6],[7,8]]))
print(minArrows([[1,2],[2,3],[3,4],[4,5]]))
print(minArrows([[1,2],[2,3],[3,4],[4,5]]))