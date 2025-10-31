"""

Leetcode 944: Delete Columns to Make Sorted

Question:
You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

abc
bce
cae

Return the minimum number of columns that can be deleted to make all the strings of the grid sorted.

"""

def minDeletionSize(strs):
    # init count
    count = 0
    # traverse the strings
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if strs[j][i] < strs[j-1][i]:
                count += 1
                break
    return count

print(minDeletionSize(["abc", "bce", "cae"]))
print(minDeletionSize(["abc", "bce", "cae"]))
