"""
X = <A,B,C,B,D,A,B>
Y = <B,D,C,A,B,A>
s[i,j] -> lcs of first i char in X and j char in Y

if X[i] == Y[j], (if there is a char match)
    s[i,j] = s[i-1,j-1] + 1
if there is a mismatch X[i] != Y[j],
    s[i,j] = max(s[i-1,j], s[i,j-1])
"""

def lcs(X, Y):
    m, n = len(X), len(Y)
    s = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                s[i][j] = s[i-1][j-1] + 1
            else:
                s[i][j] = max(s[i-1][j], s[i][j-1])
    
    return s[m][n]

print(lcs("ABCBDAB", "BDCABA"))