"""
leetcode 621: Task Scheduler

Question:
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
"""

from collections import Counter
import heapq

def taskScheduler(tasks, n):
    if n == 0:
        return len(tasks)

    freq = Counter(tasks)

    # max-heap of available tasks: (-count, task)
    avail = [(-cnt, ch) for ch, cnt in freq.items()]
    heapq.heapify(avail)

    # cooldown min-heap: (ready_time, -count, task)
    cool = []
    time = 0

    while avail or cool:
        # release any cooled tasks back to avail
        while cool and cool[0][0] <= time:
            ready, neg_cnt, ch = heapq.heappop(cool)
            heapq.heappush(avail, (neg_cnt, ch))

        if avail:
            neg_cnt, ch = heapq.heappop(avail)
            cnt = -neg_cnt - 1          # we run one instance
            time += 1                   # consumed one time unit
            if cnt > 0:
                # next time this task is available:
                # ran at current time, so ready at time + n
                heapq.heappush(cool, (time + n, -cnt, ch))
        else:
            # no available task -> jump to next ready time (idle gap)
            time = cool[0][0]

    return time


print(taskScheduler(["A","A","A","B","B","B"], 2))
print(taskScheduler(["A","A","A","B","B","B"], 0))
print(taskScheduler(["A","A","A","B","B","B"], 1))
print(taskScheduler(["A","A","A","B","B","B"], 3))
print(taskScheduler(["A","A","A","B","B","B"], 4))
print(taskScheduler(["A","A","A","B","B","B"], 5))
print(taskScheduler(["A","A","A","B","B","B"], 6))
print(taskScheduler(["A","A","A","B","B","B"], 7))
print(taskScheduler(["A","A","A","B","B","B"], 8))
print(taskScheduler(["A","A","A","B","B","B"], 9))
print(taskScheduler(["A","A","A","B","B","B"], 10))