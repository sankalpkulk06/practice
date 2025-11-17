"""
leetcode 435: Non-overlapping Intervals

Question:
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:  
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: You can remove the interval [1,3] to make the rest of the intervals non-overlapping.
"""

def noOverlapIntervals(intervals):
    # sort intervals by end time in ascending order
    intervals.sort(key=lambda x: x[1])
    # init count
    attended = 0
    prev_end = -float('inf')

    for start, end in intervals:
        if start >= prev_end:
            prev_end = end
            attended += 1

    return len(intervals) - attended

print(noOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
print(noOverlapIntervals([[1,2],[1,2],[1,2]]))
print(noOverlapIntervals([[1,2],[2,3],[3,4],[4,5]]))
print(noOverlapIntervals([[1,2],[2,3],[3,4],[2,5]]))
print(noOverlapIntervals([[1,2],[2,3],[3,4],[4,5]]))
print(noOverlapIntervals([[1,2],[2,3],[3,4],[5,6]]))
print(noOverlapIntervals([[1,6],[2,3],[3,4],[5,7]]))
print(noOverlapIntervals([[1,2],[2,3],[3,4],[10,11]]))
print(noOverlapIntervals([[1,2],[2,3],[3,4],[11,12]]))
print(noOverlapIntervals([[1,5],[2,3],[1,4],[12,13]]))
