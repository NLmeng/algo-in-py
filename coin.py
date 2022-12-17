S = []
def init(n):
    global S
    S=[-1]*(n+1)

# def ncoin(x1,x2,x3,n):
#     global S
#     if n<0:
#         return 9999
#     if n==0:
#         return 0
   
#     if S[n] == -1:
#         a = ncoin(x1,x2,x3,n-x3)
#         b = ncoin(x1,x2,x3,n-x2)
#         c = ncoin(x1,x2,x3,n-x1)
#         S[n] = 1 + min(a,b,c)
#     return S[n]

def ncoin(x1,x2,x3,n):
    global S
    if n<0:
        return 9999
    if n==0:
        return 0
    g=0
    while x2*x3 <= n:
        n = n-x3
        g += 1
    
    a = ncoin(x1,x2,x3,n-x3)
    b = ncoin(x1,x2,x3,n-x2)
    c = ncoin(x1,x2,x3,n-x1)
    return g + min(a,b,c) + 1

init(20)
print(ncoin(1,5,6,18))
print(S)