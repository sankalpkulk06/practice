"""
leetcode 406: Queue Reconstruction by Height

Question:
You are given an array of people, people, which contains pairs of integers (h, k), 
where h is the height of the i-th person and k is the number of people in front of this person who have a height greater than or equal to h. 
Write a function to reconstruct the queue.

Example 1:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
"""

def reconstructQueue(people):
    # sort people by height in descending order, and k in ascending order
    people.sort(key=lambda x: (-x[0], x[1]))
    # initialize the result list
    result = []
    # traverse people
    for person in people:
        # insert the person at the k-th position
        result.insert(person[1], person)
    return result

print(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
print(reconstructQueue([[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]))
print(reconstructQueue([[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]))
