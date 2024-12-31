# 1. 30th December, 2024

def selection_sort(arr):
    
    for i in range(len(arr)):
        min_value = arr[i]
        min_index = i
        j = i   # start from ith index
        while j < len(arr):
            if min_value > arr[j]:  # get min_value and index
                min_value = arr[j]
                min_index = j
            j = j + 1
        arr[i], arr[min_index] = arr[min_index], arr[i]     # swap
    
arr = [5,3,8,6,7,2]
selection_sort(arr)
print(arr)