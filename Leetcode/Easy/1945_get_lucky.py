"""
1945. Get Lucky

You are given a string s consisting of lowercase English letters, and an integer k. 
Your task is to convert the string into an integer by a special process, 
and then transform it by summing its digits repeatedly k times. 
More specifically, perform the following steps:

Convert s into an integer by replacing each letter with its position in the alphabet (i.e. replace 'a' with 1, 'b' with 2, ..., 'z' with 26).
Transform the integer by replacing it with the sum of its digits.
Repeat the transform operation (step 2) k times in total.
For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:

Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
Transform #2: 17 ➝ 1 + 7 ➝ 8
Return the resulting integer after performing the operations described above.

Example 1:

Input: s = "iiii", k = 1

Output: 36

Explanation:

The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.
"""

def getLucky(s, k):

    num_str = ''
    for char in s:
        char_num = str(ord(char) - ord('a') + 1)
        num_str += char_num
        # print(num_str)
    
    curr_sum = 0
    for digit in num_str:
        curr_sum += int(digit)

    for _ in range(k-1):
        new_sum = 0
        for digit in str(curr_sum):
            new_sum += int(digit)
        curr_sum = new_sum
    return curr_sum

print(getLucky("leetcode", 2))