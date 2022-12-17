def CMV(P):
    n = len(P)
    Table = [0]*n
    for i in range(1,n):
        for j in range(1,i+1):
            if P[j] + Table[i-j] > Table[i]:
                Table[i] = P[j] + Table[i-j]

    return Table

P = [0,100,200,800,900,1100,1200,1200,1100]
print(CMV(P))
P = [0,200,300,400,500,600,700,800,900]
print(CMV(P))