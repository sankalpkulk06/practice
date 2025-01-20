"""
118. Pascal Triangle

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
"""

def generate(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i+1)
        print(row)

        for j in range(1, i):
            print(j)
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
        print(triangle)
    return triangle

print(generate(5))