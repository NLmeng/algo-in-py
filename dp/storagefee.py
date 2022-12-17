import math
# A[c(1),c(2),...,c(n)]


COST = []
lo = []
def computeCost(A,S,C,F):
    global COST, lo
    m = len(A)
    COST = [None]*m
    lo   = [0]*m
    leftOver = 0 #remaining from prev month
    i = 0
    while i < m: 
        if A[i] == 0: # COST[i] = min(COST[i-1], leftOver*C+COST[i-1])
            if leftOver*C < F:
                COST[i] = COST[i-1] + leftOver*C
            else:
                COST[i] = COST[i-1]
                leftOver = 0
            lo[i] = lo[i-1]
        else: # COST[i] = min(F+COST[i-1], leftOver*C+COST[i-1]) 
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
                    COST[i] = COST[i-1] + F
                    lo[i] = i
                else:
                    COST[i] = COST[i-1] + leftOver*C
                    lo[i] = lo[i-1]
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
        if (lo[i] != lo[next]):
            next = lo[i]
    # print(lo)
    return plan
    

A = [6,2]
print("13", computeCost(A, 4, 3, 7), "plan: ", planPurchases(A))

A = [3,5,4]
print("16", computeCost(A, 10, 1, 6), "plan: ", planPurchases(A))

A = [8,6,3,1]
print("26", computeCost( A, 5, 2, 8), "plan: ", planPurchases(A))

A = [8,0,6,0,3,1]
# 8+8+8+8+2 > 8+8+8+2
print("?", computeCost(A, 5, 2, 8), "plan: ", planPurchases(A))

A = [8,0,6,0,3,1]
# 80+80+8+8+2
print("?", computeCost(A, 5, 2, 80), "plan: ", planPurchases(A))

A = [8,0,6,0,3,1]
# 80+80+8+8+2
print("?", computeCost(A, 5, 20, 80), "plan: ", planPurchases(A))