
Va = []
Vb = []
def findMax(A,B,c):
    global Va, Vb
    n = len(A)
    Va = [None]*n
    Vb = [None]*n
    findMaxHelper(A,B,c,n-1)
    # print(Va,Vb)
    findloc(Va,Vb)

def findMaxHelper(A,B,c,i):
    global Va, Vb
    if i == 0:
        return 0
    elif i > 0 and i <= 2:
        Va[i] = findC(A,1,i)
        Vb[i] = findC(B,1,i)
        findMaxHelper(A,B,c,i-1) 
    elif i > 2:
        findMaxHelper(A,B,c,i-1)
        Va[i] = findC(A,i,i) + max(Va[i-1], Vb[i-1]-c)
        Vb[i] = findC(B,i,i) + max(Vb[i-1], Va[i-1]-c)
        return
    
def findMaxIterative(A,B,c):
    n = len(A)
    Va = [None]*n
    Vb = [None]*n
    for i in range(0,n):
        if i < 3:
            Va[i] = 0
            Vb[i] = 0
        elif i == 3:
            Va[i] = findC(A,1,3)
            Vb[i] = findC(B,1,3)
        else:
            if Vb[i-1]-c < Va[i-1]:
                Va[i] = A[i] + Va[i-1]
            else:
                Va[i] = A[i] + Vb[i-1]-c
            if Va[i-1]-c < Vb[i-1]:
                Vb[i] = B[i] + Vb[i-1]
            else:
                Vb[i] = B[i] + Va[i-1]-c
    findloc(Va,Vb)

def findloc(Va,Vb):
    n = len(Va)
    loc = ""
    for i in range(1,n):
        if (Va[i] > Vb[i]):
            loc += "A "
        else:
            loc += "B "
    print(loc)

def findC(A,i,j):
    t = 0
    for k in range(i, j+1):
        if A[k] == 1:
            t +=1
    return t

# A=[0,1,1,1,2,3,4,5,6,6]
# B=[0,1,1,2,3,4,4,4,4,5]
A=[0,1,0,0,1,1,1,1,1,0]
B=[0,1,0,1,1,1,0,0,0,1]
c=0.6
findMax(A,B,0.6)
findMaxIterative(A,B,0.6)