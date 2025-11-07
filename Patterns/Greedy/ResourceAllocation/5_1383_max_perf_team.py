"""
leetcode 1383: Maximum Performance of a Team

Question:
You are given two integers n and k and two integer arrays speed and efficiency both of length n. 
There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Return the maximum performance of a team given the constraint that any two engineers in the team must have a working experience of at least engineer[j][0].

Example 1:
Input: n = 6, k = 2, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2]
Output: 60
Explanation:
Choose the engineers 1 and 5 for the team, working experience value is 2 + 5 = 7.
Performance = 7 * (2 + 5) = 49.
"""


def maxPerformance(n, k, speed, efficiency):
    
    import heapq

    # pair and sort by efficiency -> desc
    engineers = sorted(zip(efficiency, speed), reverse=1)
    print(engineers)

    # init
    min_heap = []   # holds speeds (smallest at top)
    sum_speed = 0
    max_perf = 0

    # go through all the engineers
    for eff, speed in engineers:
        # print(f'eff: {eff}, speed: {speed}, ')
        # add curr speed
        heapq.heappush(min_heap, speed)
        sum_speed += speed

        # print(f'min_heap: {min_heap}')
        # print(f'sum_speed: {sum_speed}')

        # keep only top k
        if len(min_heap) > k:
            sum_speed -= heapq.heappop(min_heap)
        
        # print(f'max_perf: {max_perf}, perf: {sum_speed * eff}')
        max_perf = max(max_perf, sum_speed * eff)


    return max_perf % (10**9+7)

print(maxPerformance(6, 2, [2,10,3,1,5,8], [5,4,3,9,7,2]))
print(maxPerformance(6, 3, [2,10,3,1,5,8], [5,4,3,9,7,2]))
print(maxPerformance(6, 4, [2,10,3,1,5,8], [5,4,3,9,7,2]))
print(maxPerformance(6, 5, [2,10,3,1,5,8], [5,4,3,9,7,2]))
print(maxPerformance(6, 6, [2,10,3,1,5,8], [5,4,3,9,7,2]))
print(maxPerformance(6, 7, [2,10,3,1,5,8], [5,4,3,9,7,2]))
print(maxPerformance(6, 8, [2,10,3,1,5,8], [5,4,3,9,7,2]))
print(maxPerformance(6, 9, [2,10,3,1,5,8], [5,4,3,9,7,2]))
print(maxPerformance(6, 10, [2,10,3,1,5,8], [5,4,3,9,7,2]))
print(maxPerformance(6, 11, [2,10,3,1,5,8], [5,4,3,9,7,2]))
print(maxPerformance(6, 12, [2,10,3,1,5,8], [5,4,3,9,7,2]))
print(maxPerformance(6, 13, [2,10,3,1,5,8], [5,4,3,9,7,2]))