"""
Traced sliding window for LeetCode 1343 (Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold)

Question:
Given an array of integers arr and two integers k and threshold, 
return the number of sub-arrays of size k and average greater than or equal to threshold.

Example:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3

"""

def numOfSubarrays(arr, k, threshold):

    # initial window
    window_avg = sum(arr[:k])/k
    count = 0 
    if window_avg >= threshold:
        count += 1
    
    for i in range(k, len(arr)):
        # slide the window
        window_avg += (arr[i] - arr[i-k])/k
        if window_avg >= threshold:
            count += 1
    
    return count

arr = [2,2,2,2,5,5,5,8]
res = numOfSubarrays(arr, 3, 4)
print(res) 

arr2 = [11,13,17,23,29,31,7,5,2,3]
res2 = numOfSubarrays(arr2, 3, 5)
print(res2) 

"""
Question:

1. Why can we multiply threshold by k instead of dividing sum by k?
Answer:
    - We can multiply threshold by k because we are checking if the average of the window is greater than or equal to threshold.

2. How many subarrays of size k exist in an array of size n?
Answer:
    - There are n-k+1 subarrays of size k in an array of size n.    

3. What changes if the condition were strictly greater (>) instead of ≥?
Answer:
    - If the condition were strictly greater (>) instead of ≥, we would not need to check if the average is greater than or equal to threshold.
    - We would only need to check if the average is greater than threshold.

4. Could this be done with a prefix sum array instead of a window? Why or why not?
Answer:
    - Yes, we could use a prefix sum array instead of a window.
    - The prefix sum array would store the sum of the elements up to the current index.
    - We could then use the prefix sum array to calculate the average of the window in constant time.


"""