"""
target = 4
change = [1,2,5]

output = 2, because 2+2

eg.
target = 13
change = [1,4,5]

output = 3, because 5+4+4
"""

def change_target(target, change):

    # res = 0
    # while target > 0:
        
    #     for i in range(1, len(change)+1):
    #         # print(change[-i])
    #         if target >= change[-i]:
    #             target = target - change[-i]
    #             res += 1
    #         # if target == 0:
    # return res

    change.sort(reverse=True)

    res = 0

    for coin in change:

        while target >= coin:
            target -= coin
            res += 1
        
        if target == 0:
            return res
    return -1

print(change_target(4, [1,2,5]))
print(change_target(13, [1,4,5]))