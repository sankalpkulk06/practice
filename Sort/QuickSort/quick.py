"""
- Divide and Conquer Algorithm (breaks down into smaller problems)
- Time complexity:  
    wort case O(n^2)
    best and avg case O(nlogn)

Basic Principle:
1. Choose a pivot element (usually last or random ele)
2. Stores eles less than the pivot ele in the left subarray and
   Stores eles greater than the pivot ele in the right subarray
3. Call quicksort recursively on left subarray and
   Call quicksort recursively on right subarray

Logic:
- lets choose pivot element as the last element
- i -> looks for element is lesser than pivot
- j -> looks for element is greater than pivot
- loop condition, till j is left of i (j<i)
- iterate i till we find an element that is NOT lesser than pivot, 
  if we find an element greater then pivot,
  then we swap arr[i] and arr[j]
- iterate j till we find an element that is NOT greater than pivot,
  if we find an element lesser than pivot,
- once j is left of i, swap arr[i] with arr[pivot]
(now we see that every ele left of pivot is lesser than pivot ele and,
every ele right of pivot is greater than pivot ele)
- now we recursively call quicksort on left subarray and right subarray


For exmaple,
pivot ele = 44
   [22,11,88,55,77,33,44]
    i              j  p         (is 22 < 44, yes. leave it left of pivot)
       i           j  p         (is 11 < 44, yes. leave it left of pivot)
          i        j  p         (is 88 < 44, no. now swap the ele arr[i] and arr[j])
             i     j  p         (is 88 < 44, no. now swap the ele arr[i] and arr[j])


"""

def quicksort(arr, left, right):

    if left < right:
        partition_pos = partition(arr, left, right)
        quicksort(arr, left, partition_pos - 1)
        quicksort(arr, partition_pos + 1, right)

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while (i < j):
        while (i < right) and (arr[i] < pivot):
            i = i+1
        while (j > left) and (arr[j] >= pivot):    
            j = j-1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i

arr = [22,11,88,55,77,33,44]
quicksort(arr, 0, len(arr) - 1)
print(arr)
