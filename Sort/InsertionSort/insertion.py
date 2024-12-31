""""
- Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands. 
- we split the list into sorted and unsorted section, [sorted | unsorted]
- The time complexity of insertion sort is O(n²) in the worst
- The spce complexity of insertion sort is O(1)

for example:
[2,6,5,1,3,4]
   |
[2,6,5,1,3,4]
     |
[2,5,6,1,3,4] => if 6 > 5, swap. No more swap needed 
       |
[1,2,5,6,3,4] => if 6 < 1, swap. if 5 < 1, swap. if 2 < 1, swap. 
         |
.
.
.


In outer loop, we loop from index 1 to n (unsorted array).
From ith element, we need to loop back and swap will we sort the array.
Hence, j = i

in sorted section, we check:(conditions)
- if arr[j-1] < arr[j]
- loop back will j>0 (out of bounds)


"""

def insertion_sort(arr):

    n = len(arr)

    # loop from 1 to n
    for i in range(1, n):
        # to loop back from the ith index
        j = i

        # loop backwards, swaping eles into position
        while (j > 0):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            # iterate backwards
            j = j - 1

arr = [2,6,5,1,3,4]
insertion_sort(arr)
print(arr)
