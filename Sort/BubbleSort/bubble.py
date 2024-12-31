"""
Time complexity: O(n^2)
Swapping sort:

Logic: 
- iterate through the list n times
- check if element at index j > j + 1, then swap
- iterate till n-i-1

for example, if we have a list 
[5,6,1,3]
iteration 1: if 5 > 6, then swap (NO SWAP) [5,6,1,3]
iteration 1: if 6 > 1, then swap (SWAP) [5,1,6,3]
iteration 1: if 6 > 3, then swap (SWAP) [5,1,3,6]

iteration 2: if 5 > 1, then swap (SWAP) [1,5,3,6]
iteration 2: if 5 > 1, then swap (SWAP) [1,3,5,6]
"""



def bubbleSort(arr):
    
    for i in range(len(arr)):
        swapped = False
        for j in (range( len(arr)-i-1)):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):  # if we have looped without swapping, then the list is sorted
            break
    print(arr)

# list = [5,6,1,3]
list = [123,83,3982,20830,92]
# print(bubbleSort(list))
bubbleSort(list)

