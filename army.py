import numpy as np

def computeP(M, N, alpha_M):

    # if M < 0 or N < 0:
    #     return "invalid"

    alpha_N = 1 - alpha_M
    P = np.zeros((M+1, M+N+1))
    P[:,0] = 1 # first row
    P[0,:] = 0 # first column
    for i in range(1, M+1):
        for j in range(1, M+N):
            P[i,j] = alpha_M * P[i,j-1] + alpha_N * P[i-1,j+1]
    print(P)
    print(len(P)*len(P[0]))
    # return P[1:,1:N+1]
    return P[M,N]

# def computeP(M,N,alpha_M):
#     cache = {'1-1': alpha_M}

#     for i in range(1, N+M+1):
#         cache['0-'+str(i)] = 0
#         cache[str(i)+'-0'] = 1
#     for i in range(1, M+1):
#         for j in range(1, N+(M-i)+1):
#             current = str(i) + "-" + str(j)
#             win     = str(i) + "-" + str(j-1)
#             loss    = str(i-1) + "-" + str(j+1)
#             cache[current] = alpha_M*cache[win] + (1-alpha_M)*cache[loss]
#     print(len(cache))
#     return cache[str(M)+"-"+str(N)]
 
# print(computeP(100000, 1000, 0.6))
print(computeP(5000, 100, 0.6)) #0.9999999999999998
print(computeP(3, 2, 0.6)) #0.6364799999999999

# 13007700
# 0.9999999999999998
# 19
# 0.6364799999999999