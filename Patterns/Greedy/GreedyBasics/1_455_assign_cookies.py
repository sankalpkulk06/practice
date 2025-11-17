"""
Leetcode 455: Assign Cookies

Question:
Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; 
and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.

Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you can only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: g = [1,2,3], s = [1,2,3]
Output: 3
Explanation: You have 3 children and 3 cookies. The greed factors of 3 children are 1, 2, 3. 
And since the cookies' size are 1, 2, 3, you can make all the children content.
You need to output 3.
"""

def assignCookies(g, s):

    # - sort g and s
    # - 2 pointers, one for each
    # - traverse:
    #     - if s[j] >= g[i], then inc count and move both counters
    #     - else, move only s pointer
    # - return count

    # sort both lists
    g.sort()
    s.sort()

    # init 2 pointers
    i = 0
    j = 0

    # init count
    count = 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    
    return count



print(assignCookies([1,2,3], [1,1]))
print(assignCookies([1,2,3], [1,2,3]))
