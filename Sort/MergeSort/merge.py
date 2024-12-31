"""
- The time and space complexity of merge sort are O(n log n) and O(n)
- Divide and Conquer Approach
    1. Divide: Divide the list or array recursively into two halves until it can no more be divided.
    2. Conquer: Each subarray is sorted individually using the merge sort algorithm.
    3. Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged.

Logic:
- Split array in half
- Call Merge Sort on each half to sort them recursively
- Merge both sorted halves into one sorted array

For example,
    [ 2,6,5,1,7,4,3 ]
            |
[ 2,6,5,1 ] [ 7,4,3 ]           # Split (Divide)
     |           |
[2,6] [5,1]  [7,4] [3]
2 | 6 5 | 1   7 | 4

[2,6] [1,5]   [4,7] [3]         # Merge (Conquer) (Compare the left most elements of the 2 arrays)
     |             |
  [1,2,5,6]     [3,4,7]
            |
     [1,2,3,4,5,6,7]


"""
def merge_sort(arr):

    # len of arr
    n = len(arr)
    midpoint = n//2

    # Length has to be greater then 1, if there is only 1 element then the list is already sorted
    if n > 1:

        # split the arrays at midpoint
        left_arr = arr[:midpoint]
        right_arr = arr[midpoint:]

        # recursion over left and right array
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Merge: Compare the left most elements of the 2 arrays
        i = 0 # track leftmost ele of left arr
        j = 0 # track leftmost ele of right arr
        k = 0 # track index of merged arr

        while i<len(left_arr) and j<len(right_arr):

            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i = i+1
            else:
                arr[k] = right_arr[j]
                j = j+1

            k = k+1

        # Merge the 2 arrays into arr
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i+1
            k = k+1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j+1
            k = k+1
        

arr = [ 2,6,5,1,7,4,3 ]
merge_sort(arr)
print(arr)