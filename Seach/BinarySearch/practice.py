# 1. 30th December, 2024

def binary_seach(arr, key):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        
        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid -1

    return -1


arr = [2,5,7,23,54,65,76,85,100]
# key = 100
key = 5
print(binary_seach(arr, key))