
OPT = []
def maxBadge(P):
    global OPT
    n = len(P)
    OPT = [0] * n

    for i in range(1, n):
        if abs(P[i]) <= i:
            OPT[i] = 1
            for j in range(1, i):
                if OPT[j] != 0 and abs(P[i] - P[j]) <= abs(i-j) and OPT[j] + 1 > OPT[i]:
                    OPT[i] = OPT[j] + 1
    return OPT[n-1]

def listBadges(P):
    global OPT
    n = len(P)
    badges = []
    maxRemaining = OPT[n-1]
    badges.append(n-1)
    maxRemaining-=1

    current = n-1
    next   = current - 1
    while maxRemaining > 0:
        if OPT[next] == maxRemaining:
            if abs(P[current]-P[next]) <= abs(current-next):
                badges.append(next)
                maxRemaining-=1
                current=next
        next-=1
    return badges


P = [0, 1,-1]
print(maxBadge(P), "\n", OPT, "PICK:", listBadges(P))

P = [0, -1, 2, 3, 2]
print(maxBadge(P), "\n", OPT, "PICK:", listBadges(P))

P = [0, 1, -4, -1, 4, 5, -4, 6, 7, -2]
print(maxBadge(P), "\n", OPT, "PICK:", listBadges(P))