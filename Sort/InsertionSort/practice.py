
# 1. 30th December, 
def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = i   # start looping back from ith postion

        # while j-1 in bounds
        while j > 0:

            # if right element is greater than left element, if yes then swap.
            if arr[j-1] > arr[j]:  
                arr[j-1], arr[j] = arr[j], arr[j-1]     # swap
                
            j = j - 1   # traverse backwards
    return arr



list = [3,4,2,1,5,9,7,8,6]
print(insertion_sort(list))