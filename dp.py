L = []
S = []
N = []
def maxProfit(A):
    n = len(A)
    L = [0] * n
    N = [0] * n
    S = [0] * n
    L[0] = A[0][1]
    S[0] = A[0][0]
    for i in range(1, n-1):
        L[i] = max(A[i][1] + N[i-1], S[i-1], L[i-1])
        S[i] = A[i][0] + max(S[i-1], L[i-1], N[i-1])
        N[i] = max(S[i-1], L[i-1], N[i-1])
    print("L:", L, "S:", S, "N:", N)
    return max(L[n-1], S[n-1], N[n-1])

A = [(10,5), (10,25), (5,30)]
print(maxProfit(A))