
# 1. 30th December, 2024

"""
[3,1,4,2]

[3,1] [4,2]
3 1    4 2      i=0 j=0 k=0 [1,,,]

[1,3] [2,4]
[1,2,3,]

[1,2,3,4]

"""

def merge_sort(arr):
    
    if len(arr) > 1:
        left_arr = merge_sort(arr[:len(arr)//2])         # first element to midpoint (excluded)
        right_arr = merge_sort(arr[len(arr)//2:])    # midpoint (included) to last element 
        # merge(arr, left_arr, right_arr)


    
        i = 0   # track leftmost ele in left array
        j = 0   # track leftmost ele of right array
        k = 0   # trak the index of main array

        while i < len(left_arr) and j < len(right_arr):
            
            if left_arr[i] <= right_arr[j]:
                arr[k] = left_arr[i]
                i = i + 1
                k = k + 1
            else:
                arr[k] = right_arr[j]
                j = j + 1
                k = k + 1

        # Merge the 2 arrays into arr
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i = i+1
            k = k+1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j = j+1
            k = k+1
    
    return arr
        

arr = [ 2,6,5,1,7,4,3 ]
merge_sort(arr)
print(arr)