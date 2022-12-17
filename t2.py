
# 2.1 True, 
# 2.2 True, 
# 2.3 True, 
# 2.4 False?, 
# 2.5 True

# 3.1sometimes
# 3.2
# A. j<=1
# B. M[i][j]+max{S[i-1,j-1],S[i,j-1], S[i+1,j-1]}, j>1 and j<=n


def returnPath(M,S):
    m=len(M)
    n=len(M[0])
    k = 0
    for i in range(1, m):
        if S[i][n-1] > S[k][n-1]:
            k = i
    print(S[k][n-1])
    soln = [-1]*n
    soln[n-1] = S[k][n-1] # soln[n] = S[k][n]
    nextCol  = n-1
    nextRow  = [k]
    while nextCol >= 0: #1
        nextCol-=1
        nextR = 0
        for r in range (0, len(nextRow)):
            term1 = S[nextRow[r]-1][nextCol]
            term2 = S[nextRow[r]][nextCol]
            term3 = S[nextRow[r]+1][nextCol]
            # print(term1, term2, term3)
            if term1 > term2 and term1 > term3:
                nextRow[r] = nextRow[r]-1
                if soln[nextCol] < term1:
                    nextR = r
                    soln[nextCol] = term1
            elif term3 > term1 and term3 > term2:
                nextRow[r] = nextRow[r]+1
                if soln[nextCol] < term3:
                    nextR = r
                    soln[nextCol] = term3
            else:
                if soln[nextCol] < term2:
                    nextR = r
                    soln[nextCol] = term2
        if term1 == term2:
            nextRow = [nextRow[r]-1, nextRow[r]]
        elif term2 == term3:
            nextRow = [nextRow[r], nextRow[r]+1]
        elif term1 == term3:
            nextRow = [nextRow[r]-1, nextRow[r]+1]
        else:
            nextRow = [nextRow[nextR]]
    return soln
       


M = [
    [-1,-1,-1,-1],
    [2,6,4,5],
    [3,9,1,6],
    [4,8,2,7],
    [1,2,3,9],
    [-1,-1,-1,-1]
]
S = [
    [-1,-1,-1,-1],
    [2,9,17,22],
    [3,13,14,23],
    [4,12,15,22],
    [1,6,15,24],
    [-1,-1,-1,-1]
]

print(returnPath(M,S))
# cP(M)
    