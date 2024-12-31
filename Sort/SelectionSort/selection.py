"""
- No Swapping
- Find min value in every iteration and swap it with the ith iteration

for example,
[5,3,8,6,7,2]
iteration 0, min value = 2. Swap it with arr[0]
[2,3,8,6,7,5]
iteration 1, min value = 3. Swap it with arr[1]
[2,3,8,6,7,5]
iteration 2, min value = 5. Swap it with arr[2]
.
.
.
[2,3,5,6,7,8]
"""

def selection_sort(arr):
    
    for i in range(len(arr)):
        min_index = i
        j = i   # start from ith index
        while j < len(arr):
            if arr[min_index] > arr[j]:  # get min_value and index
                min_index = j
            j = j + 1
        arr[i], arr[min_index] = arr[min_index], arr[i]     # swap
    
arr = [5,3,8,6,7,2]
selection_sort(arr)
print(arr)