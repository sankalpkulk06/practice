"""

leetcode 646: Maximum Length of Pair Chain

Question:
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.

A pair p is a successor of pair q if and only if q.right < p.left.

A pair p is a predecessor of pair q if and only if q.left < p.right.

Return the number of unique pairs (p, q) such that p is a successor of q or q is a successor of p.

Example 1:
Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: There are two unique pairs (1, 2) and (2, 3) that satisfy the conditions.
"""

def maxLenPairChain(pairs):
    # sort pairs by end time in ascending order
    pairs.sort(key=lambda x: x[1])
    # init count
    count = 0
    prev_end = -float('inf')
    for start, end in pairs:
        if start > prev_end:
            prev_end = end
            count += 1
    return count

print(maxLenPairChain([[1,2],[2,3],[3,4]]))
print(maxLenPairChain([[1,2],[2,3],[3,4],[4,5]]))
print(maxLenPairChain([[1,2],[2,3],[3,4],[4,5],[5,6]]))
print(maxLenPairChain([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
print(maxLenPairChain([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8]]))
print(maxLenPairChain([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9]]))
print(maxLenPairChain([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10]]))
print(maxLenPairChain([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11]]))
print(maxLenPairChain([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12]]))
print(maxLenPairChain([[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12],[12,13]]))