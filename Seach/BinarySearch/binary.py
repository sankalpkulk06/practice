"""
Binary Search Algorithm is a searching algorithm used in a sorted array by 
repeatedly dividing the search interval in half. 
The idea of binary search is to use the information that the array is sorted and reduce 
the time complexity to O(log N). 

Logic:
- Divide the search space into two halves by finding the middle index “mid”. 
- Compare the middle element of the search space with the key. 
- If the key is found at middle element, the process is terminated.
- If the key is not found at middle element, choose which half will be used as the next search space.
    - If the key is smaller than the middle element, then the left side is used for next search.
    - If the key is larger than the middle element, then the right side is used for next search.
- This process is continued until the key is found or the total search space is exhausted.
"""

def binary_search(arr, key):

    low = 0
    high = len(arr) - 1

    if len(arr) == 1 and arr[0] == key:
        return 0
    elif len(arr) == 1 and arr[0] != key:
        return -1
    
    while low <= high:

        mid = (low + high) // 2
        
        if arr[mid] == key:
            return mid
        
        elif arr[mid] > key:
            high = mid - 1

        else:
            low = mid + 1
    
    return -1

arr = [2, 3, 4, 10, 40]
key = 10
key_index = binary_search(arr, key)
print(key_index)