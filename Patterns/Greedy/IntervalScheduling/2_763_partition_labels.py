"""
leetcode 763: Partition Labels

Question:
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.   
Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Example 1:
Input: s = "abac"
Output: [1,1,2]
Explanation: The partition is "a", "ba", "c". This is a partition so that each letter appears in at most one part.
"""

def partitionLabels(s):
    
    intervals = {}
    # record [start, end] interval for each ch in s
    for i, ch in enumerate(s):
        if ch not in intervals:
            intervals[ch] = [i+1,i+1]
        else:
            intervals[ch][1] = i+1
    # print(intervals)

    # sort the intervals by start index
    intervals = sorted(intervals.values(), key = lambda x: x[0])
    # print(intervals)

    # merge overlapping intervals
    # lengths are partition sizes
    res = []
    currL, currR = intervals[0]

    for L, R in intervals[1:]:
        # overlap
        if L <= currR:
            currR = max(currR, R)
            # print(currL, currR, L, R)
        else:   # disjoint
            res.append(currR - currL + 1)
            currL, currR = L, R
            # print(res)
    res.append(currR - currL + 1)
    # print(res)
    return res

print(partitionLabels("abac"))
print(partitionLabels("abacaba"))
print(partitionLabels("abc"))
print(partitionLabels("aab"))
print(partitionLabels("ababcbacadefegdehijhklij"))
print(partitionLabels("ababcb"))
print(partitionLabels("ababc"))
