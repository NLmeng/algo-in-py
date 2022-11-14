import math
# A[c(1),c(2),...,c(n)]
# def computeCost(A,S,C,F):
#     m = len(A)
#     lastOrder = [None]*m
#     Cost      = [None]*m

#     if A[0] == 0:
#         Cost[0] = 0
#         lastOrder[0] = None
#     else:
#         Cost[0] = F
#         lastOrder[0] = 1

#     for i in range(1, m):
#         if lastOrder[i-1] == None:
#             if A[i] == 0:
#                 Cost[i] = 0
#                 lastOrder[i] = None
#             else:
#                 Cost[i] = F
#                 lastOrder[i] = i
#         elif A[lastOrder[i-1]] + A[i] > S or F < C * (i - lastOrder[i-1]) * A[i]:
#             Cost[i] = Cost[i-1] + F
#             lastOrder[i] = i
#         else:
#             Cost[i] = Cost[i-1] + C * (i - lastOrder[i-1]) * A[i]
#             lastOrder[i] = lastOrder[i-1]
#     print("C", Cost, "O", lastOrder)
#     return Cost[m-1]

COST = []
lo = []
def computeCost(A,S,C,F):
    global COST, lo
    m = len(A)
    COST = [None]*m
    lo   = [0]*m
    leftOver = 0
    i = 0
    while i < m:

        if leftOver == 0:
            j = i + 1
            while j < m and leftOver + A[j] < S:
                leftOver += A[j]
                j+=1

            if i == 0:
                COST[i] = F
            else:
                COST[i] = COST[i-1] + F
            lo[i] = i
        else:
            if (F+COST[i-1] < leftOver*C+COST[i-1]):
                lo[i] = i
            else:
                lo[i] = lo[i-1]
            COST[i] = min(F+COST[i-1], leftOver*C+COST[i-1]) #remaining quantity from prev
            leftOver -= A[i]

        i+=1

    return COST

def planPurchases(A):
    global COST, lo
    m = len(A)
    plan = [0]*m
    i = m-1
    next = lo[i]
    while i >= 0:
        plan[next] += A[i]
        i-=1
        if next-1>=0 and (lo[i] != lo[next]):
            next = lo[i]
    # print(lo)
    return plan
    


A = [6,2]
print("13", computeCost(A, 4, 3, 7), "plan: ", planPurchases(A))

A = [8,6,3,1]
print("26", computeCost(A, 5, 2, 8), "plan: ", planPurchases(A))

A = [3,5,4]
print("16", computeCost(A, 10, 1, 6), "plan: ", planPurchases(A))