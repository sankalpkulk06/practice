"""
1539. Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9
"""

def findKthPositive(arr, k):
    
    missing = 0
    current_num = 1
    index = 0

    while missing < k:
        if index < len(arr) and arr[index] == current_num:  # num in array
            index += 1
            print("num in arr: ", arr[index])
        else:
            missing += 1    # found missing num
            print("missing: ", missing)
            if missing == k:
                return current_num
        current_num += 1
        print("curr num: ", current_num)


print(findKthPositive([2,3,4,7,11], 5))