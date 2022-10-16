

# i = index of interval, starting from 1
# v = weight of current interval, bigger = more priority
# p = number of intervals that are finished before this interval began
# OPT = optimal sum of v
# M = memoize for recursion, store the OPT of current subproblems

# @param an array of intervals
# @return reset memoize and solve for optimal set of intervals
def solve(Array, memoize):
    memoize = []
    itrComputeOPT(Array)
    print("memoize", M)
    print("pick intervals:", findSolution(len(Array)))

# @param Array of (i, v, p)
def itrComputeOPT(Array):
    M.extend([0])
    M[0] = 0
    for j in Array:
        M.extend([0])
        M[j[0]] = max(j[1] + M[j[2]], M[j[0] - 1])

# @param index j
# @return the optimal solution, searching only up to interval j
def findSolution(j):
    if j == 0:
        return 0
    else:
        if arr[j-1][1] + M[arr[j-1][2]] >= M[j - 1]:
            return j, findSolution(arr[j-1][2])
        else:
            return findSolution(j - 1)



# Array of intervals (i, v, p)
# arr = [(1,2,0), (2,4,0), (3,4,1), (4,7,0), (5,2,3), (6,3,3)]
arr = [(1,2,0), (2,1,0), (3,1,2,), (4,2,0), (5,1,3), (6,3,2)]
M   = []
solve(arr, M)