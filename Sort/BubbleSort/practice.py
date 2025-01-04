# 2. 3rd Jan, 2025
def bubble_sort(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

list = [3,4,2,1,5,9,7,8,6]
print(bubble_sort(list))


# 1. 30th December, 2024
# def bubble_sort(arr):

#     for i in range(len(arr)):

#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr

# list = [3,4,2,1,5,9,7,8,6]
# print(bubble_sort(list))
