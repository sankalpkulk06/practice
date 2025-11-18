"""
Leetcode 1385: Find the Distance Value Between Two Arrays

Question:
Given two integer arrays arr1 and arr2, and the integer d, return the distance value between two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example 1:
Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation:
For arr1[0]=4 we have:
|4-10|=6 > d=2
|4-9|=5 > d=2
|4-1|=3 > d=2
For arr1[1]=5 we have:
|5-10|=5 > d=2
|5-9|=4 > d=2
|5-1|=4 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
So there are 2 values whose distance is strictly greater than d=2, which are [5, 8].
"""

def findTheDistanceValue(arr1, arr2, d):

    # Import bisect for efficient binary search operations
    import bisect

    # Sort arr2 so we can use binary search for each element in arr1
    arr2.sort()
    count = 0  # Initialize the count of valid elements

    # Iterate over each element x in arr1
    for x in arr1:
        # Find the insertion index of x in arr2 to keep arr2 sorted
        idx = bisect.bisect_left(arr2, x)

        valid = True  # Assume x is valid initially

        # Check if the element at the insertion index (right neighbor or equal) is within distance d
        if idx < len(arr2) and abs(arr2[idx] - x) <= d:
            valid = False  # x is not valid if this condition is met

        # Check if the element just before the insertion index (left neighbor) is within distance d
        if idx > 0 and abs(arr2[idx - 1] - x) <= d:
            valid = False  # x is not valid if this condition is met

        # If x remains valid, increment the count
        if valid:
            count += 1

    # Return the number of valid elements satisfying the distance constraint
    return count
print(findTheDistanceValue([4,5,8], [10,9,1,8], 2))
print(findTheDistanceValue([1,4,5,6], [2,3,7,8,9], 3))
print(findTheDistanceValue([1,8,9,10], [1,2,3,4,5,6,7,8,9,10], 0))
print(findTheDistanceValue([1,2,3,4,5], [6,7,8,9,10], 1))
print(findTheDistanceValue([1,2,3,4,5], [6,7,8,9,10], 1))