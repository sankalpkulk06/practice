"""
leetcode 56: Merge Intervals

Question:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

def mergeIntervals(intervals):
    
    # sort by start time
    intervals.sort(key = lambda x: x[0])

    # init
    result = []
    current_start, current_end = intervals[0]

    # traverse
    for start, end in intervals:
        # overlap
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            result.append([current_start, current_end])
            current_start, current_end = start, end
    
    result.append([current_start, current_end])

    return result


print(mergeIntervals([[1,3],[2,6],[8,10],[15,18]]))
print(mergeIntervals([[1,4],[4,5]]))
print(mergeIntervals([[1,2],[2,3],[3,4],[4,5]]))
print(mergeIntervals([[1,2],[2,3],[3,4],[4,5]]))