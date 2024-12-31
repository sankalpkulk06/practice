

def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = i   # start looping back from ith postion

        while j > 0:
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            j = j - 1
    return arr



list = [3,4,2,1,5,9,7,8,6]
print(insertion_sort(list))