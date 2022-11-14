L = []
S = []
N = []

def maxProfit(A):
    global L, S, N
    n = len(A)
    L = [0] * n
    N = [0] * n
    S = [0] * n
    L[0] = A[0][1]
    S[0] = A[0][0]
    
    for i in range(1, n):
        S[i] = A[i][0] + max(S[i-1], L[i-1], N[i-1])
        # L[i] = max(A[i][1] + N[i-1], S[i], L[i-1])
        L[i] = max(A[i][1] + N[i-1], A[i][0] + S[i-1], L[i-1])
        N[i] = max(S[i-1], L[i-1], N[i-1])
    print("L:", L, "S:", S, "N:", N)
    return max(L[n-1], S[n-1], N[n-1])

# def planConcerts(A):
#     n = len(A)
#     global L, S, N
#     OPT = []
#     if len(A[0]) == 0:
#         OPT.append("N")
#     else:
#         if L[0] > S[0]:
#             OPT.append(("L", A[0]))
#         else:
#             OPT.append(("S", A[0]))

#     for i in range(1, n):
#         if len(A[i]) == 0:
#             OPT.append("N")
#         else:
#             if L[i] > S[i]:
#                 OPT[i-1] = "N"
#                 OPT.append(("L", A[i]))
#             else:
#                 OPT.append(("S", A[i]))
#     return OPT

def planConcerts(A):
    global L, S, N

    n = len(A)
    OPT = ["N"] * n
    
    i = n-1
    while i >= 0:
        if len(A[i]) == 0:
            OPT[i] = ("N")
        else:
            if L[i] > S[i]:
                OPT[i] = (("L", A[i][1]))
                i -= 1
            else:
                OPT[i] = (("S", A[i][0]))
        i-=1
    return OPT


# A[(small, large))
# pick one or the other, if large is picked then the previous picked needs to be empty/"N"
# goal: maximize sum picked
A = [(10,5), (10,25), (5,30)]
print(maxProfit(A))
print(planConcerts(A))

A = [(10,5), (1,50), (10,5), (10,1)]
print(maxProfit(A))
print(planConcerts(A))

A = [(50,5), (50,100), (9,9), (90,100)]
print(maxProfit(A))
print(planConcerts(A))