
# 1. 30th December, 2024
def quicksort(arr, left, right):

    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)


def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = right

    while i < j:    # while i and j dont cross each other

        while arr[i] < arr[pivot] and i < right:
            i = i + 1
        
        while arr[j] >= arr[pivot] and j > left:
            j = j - 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    
    # i and j have crossed
    # check if ele at i is greater than pivot, if yes then swap
    if arr[i] > arr[pivot]:
        arr[i], arr[pivot] = arr[pivot], arr[i]
    
    return i
        



arr = [22,11,88,55,77,33,44]
quicksort(arr, 0, len(arr) - 1)
print(arr)
